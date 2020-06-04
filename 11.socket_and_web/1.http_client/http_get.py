#!/usr/bin/env python
# encoding: utf-8

from urllib import request, parse

# Base URL being accessed
url = 'http://httpbin.org/post'

# Dictionary of query parameters (if any)
parms = {
    'name1': 'value1',
    'name2': 'value2'
}

# Encode the query string
querystring = parse.urlencode(parms)

# Make a Get request and read the response
u = request.urlopen(url, querystring.encode('ascii'))
resp = u.read()

print(resp)
