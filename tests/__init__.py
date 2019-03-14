from starlette.applications import Starlette
from starlette.testclient import TestClient

from starlette_jsonrpc import dispatcher
from starlette_jsonrpc.endpoint import JSONRPCEndpoint


app = Starlette()


@dispatcher.add_method
async def subtract(params):
    return {'result': params['x'] - params['y']}


@dispatcher.add_method(name='SubstractMethod')
async def second_method(params):
    return {'test': 'method'}


app.mount('/api', JSONRPCEndpoint)

client = TestClient(app)
