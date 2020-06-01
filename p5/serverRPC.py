import sys
from acciones import *
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

HOST=sys.argv[1]
PORT=int(sys.argv[2])

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths=('/RPC2',)
    
with SimpleXMLRPCServer((HOST,PORT),requestHandler=RequestHandler) as server:
    print("Servidor a la escucha")
    server.register_introspection_functions()
    server.register_instance(Acciones())
    server.serve_forever()