class JSONRPCException(Exception):

    def __init__(self, id: str = None, errors: dict = None) -> None:
        self._id = id
        self._errors = errors or {}

    @property
    def id(self):
        return self._id

    @property
    def errors(self):
        return self._errors


class JSONRPCMethodNotFoundException(JSONRPCException):
    CODE = -32601
    MESSAGE = "Method not found."


class JSONRPCInvalidParamsException(JSONRPCException):
    CODE = -32602
    MESSAGE = "Invalid params."
