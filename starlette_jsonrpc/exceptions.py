class JSONRPCMethodNotFoundException(Exception):
    CODE = -32601
    MESSAGE = "Method not found"
