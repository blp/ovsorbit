#!/usr/bin/env python

import cgi
import Cookie
import json
import os
import requests
import sys
import urlparse
import uuid
import flup.server.fcgi

import cgitb
cgitb.enable()

# Returns the session UUID, either taken from the session cookie or a
# freshly generated session.
def get_session(environ):
    cookies = Cookie.SimpleCookie()
    cookies.load(environ.get("HTTP_COOKIE", ""))
    try:
        return uuid.UUID(cookies['session'].value)
    except KeyError:
        # No session cookie.  Fine, we'll generate one.
        pass
    except ValueError:
        # Invalid UUID.  Fine, we'll start a new session.
        pass

    # Start a new session.
    return uuid.uuid4()
    
# Returns existing session state for UUID 'session'.
def read_session_state(session):
    try:
        f = open('/srv/orbit-state/%s' % session)
    except IOError:
        # No state yet.
        return {}

    state = {}
    try:
        state = json.load(f)
    except ValueError:
        # Bad JSON.  Start over with empty state.
        pass

    f.close()
    return state

session = get_session(os.environ)
state = read_session_state(session)

fields = cgi.FieldStorage()
r = None
r2 = None
access_token = ''
username = ''
if 'code' in fields:
    code = fields['code'].value
    r = requests.post('https://github.com/login/oauth/access_token',
                      headers={'Accept': 'application/json'},
                      data={'client_id': os.environ['GITHUB_CLIENT_ID'],
                            'client_secret': os.environ['GITHUB_CLIENT_SECRET'],
                            'code': code})
    access_token = r.json()['access_token']

    r2 = requests.get('https://api.github.com/user',
                      headers={'Authorization': 'token %s' % access_token,
                               'Accept': 'application/vnd.github.v3+json'})
    state['username'] = r2.json()['login']
    state['name'] = r2.json()['name']

# Start response.
print("Content-Type: text/html")
print("Set-Cookie: %s" % session)
print("")

if r:
    print str(r.json())
if r2:
    print unicode(r2.text)
print '<h1>FastCGI Environment</h1>\n'
print '<table>\n'
print '<tr><th>%s</th><td>%s</td></tr>\n' % ('access_token', str(access_token))
print '<tr><th>%s</th><td>%s</td></tr>\n' % ('username', str(username))
for k, v in sorted(os.environ.items()):
    try:
        if not k.endswith('SECRET'):
            print '<tr><th>%s</th><td>%s</td></tr>\n' % (cgi.escape(k), cgi.escape(v))
    except:
        pass
print '<tr><th>uid</th><td>%d</td></tr>' % os.getuid()
print '</table>\n'
