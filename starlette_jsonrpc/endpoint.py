from starlette.endpoints import HTTPEndpoint
from starlette.responses import JSONResponse

from starlette_jsonrpc import dispatcher
from starlette_jsonrpc.exceptions import JSONRPCInvalidParamsException
from starlette_jsonrpc.exceptions import JSONRPCMethodNotFoundException
from starlette_jsonrpc.schemas import JSONRPCErrorResponse
from starlette_jsonrpc.schemas import JSONRPCRequest
from starlette_jsonrpc.schemas import JSONRPCResponse


class JSONRPCEndpoint(HTTPEndpoint):
    async def post(self, request):
        try:
            response = await self._get_response(request)
        except JSONRPCInvalidParamsException as exc:
            return self._get_exception_response(exc)
        except JSONRPCMethodNotFoundException as exc:
            return self._get_exception_response(exc)

        return JSONResponse(response)

    @staticmethod
    async def _get_response(request):
        params = await request.json()
        id = params.get("id")

        if not id or id == "":
            return None

        data, errors = JSONRPCRequest.validate_or_error(params)

        if errors:
            raise JSONRPCInvalidParamsException(id, errors)

        method = data.get("method")
        func = dispatcher.routes_map.get(method)

        if not func:
            raise JSONRPCMethodNotFoundException(id)

        params = data.get("params")

        if isinstance(params, list):
            try:
                result = dict(await func(*params))
            except TypeError as e:
                errors = {"params": f"{e}"}
                raise JSONRPCInvalidParamsException(id, errors)
        else:
            try:
                result = dict(await func(params))
            except KeyError as e:
                errors = {"params": f"Required param: {e}"}
                raise JSONRPCInvalidParamsException(id, errors)

        response = JSONRPCResponse.validate(
            {"id": id, "jsonrpc": "2.0", "result": result}
        )
        return dict(response)

    @staticmethod
    def _get_exception_response(exc):
        response = JSONRPCErrorResponse.validate(
            {
                "jsonrpc": "2.0",
                "id": str(exc.id),
                "error": {
                    "code": exc.CODE,
                    "message": exc.MESSAGE,
                    "data": {key: value for (key, value) in exc.errors.items()},
                },
            }
        )
        return JSONResponse(dict(response))
