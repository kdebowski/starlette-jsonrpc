import typesystem


class ErrorSchema(typesystem.Schema):
    code = typesystem.Integer()
    message = typesystem.String()
    data = typesystem.Object(additional_properties=True)


class JSONRPCRequest(typesystem.Schema):
    jsonrpc = typesystem.String(pattern='2.0', trim_whitespace=False)
    id = typesystem.String(trim_whitespace=False)
    params = typesystem.Object(additional_properties=True)
    method = typesystem.String()


class JSONRPCResponse(typesystem.Schema):
    jsonrpc = typesystem.String(pattern='2.0', trim_whitespace=False)
    id = typesystem.String(trim_whitespace=False, allow_null=True)
    result = typesystem.Object()


class JSONRPCErrorResponse(typesystem.Schema):
    jsonrpc = typesystem.String(pattern='2.0', trim_whitespace=False)
    id = typesystem.String(trim_whitespace=False)
    error = typesystem.Nested(ErrorSchema)
