#!/usr/bin/env python

from cgi import escape
import Cookie
import json
import os
import sys
import urlparse
import uuid
import flup.server.fcgi

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

def app(environ, start_response):
    session = get_session(environ)
    state = read_session_state(session)

    # Start response.
    headers = [('Content-Type', 'text/html')]
    session_cookie = Cookie.SimpleCookie()
    session_cookie['session'] = str(session)
    session_cookie['session']["Path"] = '/'
    headers.extend(("Set-Cookie", morsel.OutputString())
                   for morsel
                   in session_cookie.values())
    start_response('200 OK', headers)

    yield '<h1>FastCGI Environment</h1>\n'
    yield '<table>\n'
    for k, v in sorted(environ.items()):
        try:
            if not k.endswith('SECRET'):
                yield '<tr><th>%s</th><td>%s</td></tr>\n' % (escape(k), escape(v))
        except:
            pass
    yield '<tr><th>uid</th><td>%d</td></tr>' % os.getuid()
    yield '</table>\n'

flup.server.fcgi.WSGIServer(app).run()
