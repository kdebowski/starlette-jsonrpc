from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.testclient import TestClient

from starlette_jsonrpc import dispatcher
from starlette_jsonrpc.endpoint import JSONRPCEndpoint


# Startup

app = Starlette()


@dispatcher.add_method
def my_method(request):
    return JSONResponse({'test': 'method'})


app.mount('/api', JSONRPCEndpoint)

# Testing

client = TestClient(app)

payload = {
    "jsonrpc": "2.0",
    "method": "my_method",
    "params": [],
    "id": 1
}


def test_post_call_should_return_status_code_200():
    response = client.post('/api/', json=payload)
    assert response.status_code == 200


def test_get_call_should_return_method_not_allowed():
    response = client.get('/api/')
    assert response.status_code == 405


def test_put_call_should_return_method_not_allowed():
    response = client.put('/api/', data=payload)
    assert response.status_code == 405


def test_delete_call_should_return_method_not_allowed():
    response = client.delete('/api/')
    assert response.status_code == 405


def test_patch_call_should_return_method_not_allowed():
    response = client.patch('/api/', payload)
    assert response.status_code == 405
