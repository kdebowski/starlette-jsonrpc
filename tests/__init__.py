from starlette.applications import Starlette
from starlette.testclient import TestClient

from starlette_jsonrpc import dispatcher
from starlette_jsonrpc.endpoint import JSONRPCEndpoint


app = Starlette()


@dispatcher.add_method
async def sum(params):
    return {"sum": params["x"] + params["y"]}


@dispatcher.add_method
async def subtract(params):
    return params["x"] - params["y"]


@dispatcher.add_method(name="SubtractMethod")
async def second_method(params):
    return params["x"] - params["y"]


@dispatcher.add_method
async def subtract_positional(x, y):
    return x - y


app.mount("/api", JSONRPCEndpoint)

client = TestClient(app)
