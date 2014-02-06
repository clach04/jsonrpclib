"""Ready to run demo client for jsonrpclib from
https://github.com/joshmarshall/jsonrpclib
"""

import sys
import platform

import jsonrpclib

print sys.version
#print sys.version_info
#print sys.platform
print platform.platform()

print jsonrpclib.config.version

server = jsonrpclib.Server('http://localhost:9999')
print server.helloworld(hellostring='Hello from Python json-rpc!', counter=99)
#print server.add(x=5, y=10)
