import types

from starlette.applications import Starlette
from starlette.responses import JSONResponse

from starlette_jsonrpc import dispatcher


# Startup

app = Starlette()


@dispatcher.add_method
def my_method(request):
    return JSONResponse({'test': 'method'})


# Testing


def test_adding_methods_to_dispatcher():
    func = dispatcher.routes_map.get('my_method')
    assert func is not None
    assert isinstance(func, types.FunctionType) is True
