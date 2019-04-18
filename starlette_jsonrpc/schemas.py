import typesystem


class ErrorSchema(typesystem.Schema):
    code = typesystem.Integer()
    message = typesystem.String()
    data = typesystem.Object(additional_properties=True)


class JSONRPCRequest(typesystem.Schema):
    jsonrpc = typesystem.String(pattern="2.0", trim_whitespace=False)
    id = typesystem.Union(
        any_of=[
            typesystem.String(allow_null=True, min_length=1, trim_whitespace=False),
            typesystem.Integer(allow_null=True),
        ]
    )
    params = typesystem.Union(
        any_of=[typesystem.Object(additional_properties=True), typesystem.Array()]
    )
    method = typesystem.String()


class JSONRPCResponse(typesystem.Schema):
    jsonrpc = typesystem.String(pattern="2.0", trim_whitespace=False)
    id = typesystem.Union(
        any_of=[
            typesystem.String(allow_null=True, min_length=1, trim_whitespace=False),
            typesystem.Integer(allow_null=True),
        ]
    )
    result = typesystem.Any()


class JSONRPCErrorResponse(typesystem.Schema):
    jsonrpc = typesystem.String(pattern="2.0", trim_whitespace=False)
    id = typesystem.String(trim_whitespace=False)
    error = typesystem.Reference(to=ErrorSchema)
