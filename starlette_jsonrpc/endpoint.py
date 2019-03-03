from starlette.endpoints import HTTPEndpoint
from starlette_jsonrpc import dispatcher


class JSONRPCEndpoint(HTTPEndpoint):

    async def post(self, request):
        data = await request.json()
        method = data.get('method')
        func = dispatcher.routes_map.get(method)
        return func(request)
