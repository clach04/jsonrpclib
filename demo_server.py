"""Ready to run demo server for jsonrpclib from
https://github.com/joshmarshall/jsonrpclib
"""

from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer


def helloworld(hellostring='hello world', counter=0):
    result = {}
    result['hellostring'] = 'Well "%s" to you too.' % hellostring
    result['counter'] = counter + 1
    return result

server = SimpleJSONRPCServer(('localhost', 9999))
server.register_function(helloworld)
server.register_function(pow)
server.register_function(lambda x, y: x + y, 'add')
server.register_function(lambda x: x, 'ping')
server.serve_forever()
