#! /usr/bin/python3

import datetime
import xml.dom.minidom
import os
import subprocess
import re

base_url = 'https://ovsorbit.org'
def parse_file(name):
    file = open(name)
    s = file.read().replace('${baseurl}', base_url).replace("``", "&#x201c;").replace("''", "&#x201d;")
    return xml.dom.minidom.parseString(s)

def get_optional_elem(parent, name):
    for elem in parent.childNodes:
        if elem.nodeType == elem.ELEMENT_NODE and elem.nodeName == name:
            return elem
    return None

def get_elem(parent, name):
    e = get_optional_elem(parent, name)
    assert e is not None
    return e

rss_skel = parse_file('rss-skel.xml')
episodes = []
for i in range(1, 23):
    e = parse_file('episode-%d.xml' % i)
    size = os.stat('episode-%d.mp3' % i).st_size
    runtime = int(subprocess.check_output(['mp3info', '-p', '%S', 'episode-%d.mp3' % i]))

    # Check pubDate.
    pubdate = get_elem(e.documentElement, 'pubDate').childNodes[0].data
    m = re.match('(Sun|Mon|Tue|Wed|Thu|Fri|Sat), ([0-3][0-9]) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (201[6-9]) ([0-9][0-9]:[0-9][0-9]:[0-9][0-9]) GMT$', pubdate)
    if not m:
        assert False

    fulldate = '%s %s, %s' % (m.group(3), m.group(2).lstrip('0'), m.group(4))

    y = int(m.group(4))
    if y == datetime.date.today().year:
        shortdate = '%s %s' % (m.group(3), m.group(2).lstrip('0'))
    else:
        shortdate = '%s %s' % (m.group(3), m.group(2).lstrip('0'), m.group(4))

    episodes.append({'index': i,
                     'xml': e,
                     'size': size,
                     'runtime': runtime,
                     'fulldate': fulldate,
                     'shortdate': shortdate})

rss = rss_skel.cloneNode(deep=True)
channel_node = get_elem(rss.documentElement, 'channel')
for d in episodes:
    i = d['index']
    e = d['xml'].cloneNode(deep=True)
    size = d['size']
    runtime = d['runtime']

    guests = get_optional_elem(e.documentElement, 'guests')
    if guests:
        title = get_optional_elem(e.documentElement, 'title')
        title.appendChild(e.createTextNode(', with '))
        for node in guests.childNodes:
            title.appendChild(node)
        guests.parentNode.removeChild(guests)

    # Escape all the XML in description.
    desc = get_elem(e.documentElement, 'description')
    s = ''
    for child in desc.childNodes:
        s += child.toxml()
    newDesc = e.createElement('description')
    newDesc.appendChild(e.createTextNode(s))
    desc.parentNode.replaceChild(newDesc, desc)

    # <enclosure length="32546740" type="audio/mpeg" url="https://ovsorbit.org/episode-1.mp3"/>
    elem = e.createElement('enclosure')
    elem.setAttribute('length', '%d' % size)
    elem.setAttribute('type', 'audio/mpeg')
    elem.setAttribute('url', '%s/episode-%d.mp3' % (base_url, i))
    e.documentElement.appendChild(elem)

    # This should remain constant regardless of where the podcast moves
    # to avoid changing the GUID for an episode, which confuses clients.
    #
    # <guid>http://ovsorbit.benpfaff.org/episode-1</guid>
    elem = e.createElement('guid')
    elem.appendChild(e.createTextNode('http://ovsorbit.benpfaff.org/episode-%d' % (i)))
    e.documentElement.appendChild(elem)

    # <itunes:duration>HH:MM:SS</itunes:duration>
    ss = runtime
    hh = ss / 3600
    ss -= hh * 3600
    mm = ss / 60
    ss -= mm * 60
    elem = e.createElement('itunes:duration')
    elem.appendChild(e.createTextNode('%02d:%02d:%02d' % (hh, mm, ss)))
    e.documentElement.appendChild(elem)

    # <category>Technology</category>
    elem = e.createElement('category')
    elem.appendChild(e.createTextNode('Technology'))
    e.documentElement.appendChild(elem)

    # <itunes:explicit>No</itunes:explicit>
    elem = e.createElement('itunes:explicit')
    elem.appendChild(e.createTextNode('No'))
    e.documentElement.appendChild(elem)

    # <itunes:block>No</itunes:block>
    elem = e.createElement('itunes:block')
    elem.appendChild(e.createTextNode('No'))
    e.documentElement.appendChild(elem)
    channel_node.appendChild(e.documentElement)

rss_xml = open('rss.xml', 'w')
rss_xml.write(rss.toxml())
rss_xml.close()

summary = ''
details = ''
for d in reversed(episodes):
    i = d['index']
    e = d['xml']
    size = d['size']
    runtime = d['runtime']
    shortdate = d['shortdate']
    fulldate = d['fulldate']

    title = ''
    for elem in get_elem(e.documentElement, 'title').childNodes:
        title += elem.toxml()

    guests = ''
    guests_node = get_optional_elem(e.documentElement, 'guests')
    if guests_node is not None:
        guests += ", with "
        for elem in guests_node.childNodes:
            guests += elem.toxml()

    link = '<a href="episode-%d.mp3">MP3</a>' % i
    mp3info = '%d MB, %d min' % (
        (size + 512 * 1024) / (1024 * 1024), (runtime + 30) / 60)

    summary += '''<tr>
  <td align="right"><span class="stars">
<!--stars %d-->
  </td>
  <td align="right">%d.</td><td><a href="#e%d">%s<span class="guests">%s</span></a><span class="date"> (%s)</span></td>
  <td><span title="%s">%s</span></td>
</tr>
''' % (i, i, i, title, guests, shortdate, mp3info, link)

    s = '<h3>Episode %d: <a name="e%d">%s%s (%s)</a></h3>\n' % (i, i, title, guests, fulldate)
    for elem in get_elem(e.documentElement, 'description').childNodes:
        s += elem.toxml()
    s += '<p>Listen: %s (%s).</p>' % (link, mp3info)
    details += s

file = open('index-skel.html')
s = file.read().replace('${summary}', summary).replace('${details}', details)
index_html = open('index.html', 'w')
index_html.write(s)
index_html.close()
