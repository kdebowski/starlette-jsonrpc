from json import JSONDecodeError

from starlette.endpoints import HTTPEndpoint
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.responses import Response

from starlette_jsonrpc import dispatcher
from starlette_jsonrpc.constants import JSONRPC_VERSION
from starlette_jsonrpc.exceptions import JSONRPCException
from starlette_jsonrpc.exceptions import JSONRPCInvalidParamsException
from starlette_jsonrpc.exceptions import JSONRPCInvalidRequestException
from starlette_jsonrpc.exceptions import JSONRPCMethodNotFoundException
from starlette_jsonrpc.exceptions import JSONRPCParseErrorException
from starlette_jsonrpc.schemas import JSONRPCErrorResponse
from starlette_jsonrpc.schemas import JSONRPCRequest
from starlette_jsonrpc.schemas import JSONRPCResponse


class JSONRPCEndpoint(HTTPEndpoint):
    async def post(self, request: Request) -> Response:
        try:
            response = await self._get_response(request)
        except JSONRPCInvalidParamsException as exc:
            return self._get_exception_response(exc)
        except JSONRPCMethodNotFoundException as exc:
            return self._get_exception_response(exc)
        except JSONRPCInvalidRequestException as exc:
            return self._get_exception_response(exc)
        except JSONRPCParseErrorException as exc:
            return self._get_exception_response(exc)

        return JSONResponse(response)

    async def _get_response(self, request: Request) -> dict:
        try:
            req = await request.json()
        except JSONDecodeError:
            raise JSONRPCParseErrorException()
        except Exception:
            raise JSONRPCInvalidRequestException()

        if not self._valid_request(req):
            raise JSONRPCInvalidRequestException()

        if not req:
            raise JSONRPCInvalidRequestException()

        if self._is_notification(req):
            return {}

        data, errors = JSONRPCRequest.validate_or_error(req)
        id = req.get("id")

        if errors:
            raise JSONRPCInvalidParamsException(id, errors)

        method = data.get("method")
        func = dispatcher.methods_map.get(method)

        if not func:
            raise JSONRPCMethodNotFoundException(id)

        params = data.get("params")

        result = await self._get_result(params, func, id)

        response = JSONRPCResponse.validate(
            {"id": id, "jsonrpc": JSONRPC_VERSION, **result}
        )
        return dict(response)

    @staticmethod
    def _valid_request(req) -> bool:
        if isinstance(req, dict):
            return True
        if isinstance(req, list):
            if all([isinstance(elem, dict) for elem in req]):
                return True
        return False

    @staticmethod
    def _is_notification(req: dict) -> bool:
        if all(k in req for k in ("jsonrpc", "method", "params")) and not "id" in req:
            return True
        return False

    @staticmethod
    async def _get_result(params, func, id: str = None) -> dict:
        if isinstance(params, list):
            try:
                return await func(*params)
            except TypeError as e:
                errors = {"params": f"{e}"}
                raise JSONRPCInvalidParamsException(id, errors)
        elif isinstance(params, dict):
            try:
                return await func(params)
            except KeyError as e:
                errors = {"params": f"Required param: {e}"}
                raise JSONRPCInvalidParamsException(id, errors)
        else:
            raise JSONRPCInvalidRequestException()

    @staticmethod
    def _get_exception_response(exc: JSONRPCException) -> JSONResponse:
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
