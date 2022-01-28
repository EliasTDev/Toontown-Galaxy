"""HTTPUtil.py: contains HTTP transaction utility functions"""

from pandac.PandaModules import *


class HTTPUtilException(Exception):
    def __init__(self, what): Exception.__init__(self, what)


class ConnectionError(HTTPUtilException):
    def __init__(self, what, statusCode):
        HTTPUtilException.__init__(self, what)
        self.statusCode = statusCode


class UnexpectedResponse(HTTPUtilException):
    def __init__(self, what): HTTPUtilException.__init__(self, what)


def getHTTPResponse(url, http, body=''):
    # returns the results of an HTTP request in a list of strings,
    # with trailing newlines removed
    if body:
        hd = http.postForm(url, body)
    else:
        hd = http.getDocument(url)
    if not hd.isValid():
        raise ConnectionError(
            f"Unable to reach {url.cStr()}", hd.getStatusCode())
    stream = hd.openReadBody()
    sr = StreamReader(stream, 1)
    response = sr.readlines()

    # strip trailing newlines
    for i in range(len(response)):
        if response[i][-1] == '\n':
            response[i] = response[i][:-1]

    return response
