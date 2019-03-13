import types

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.testclient import TestClient

from starlette_jsonrpc import dispatcher


# Startup
from starlette_jsonrpc.endpoint import JSONRPCEndpoint

app = Starlette()


app.mount('/api', JSONRPCEndpoint)


client = TestClient(app)

# Testing


# def test_with_positional_parameters():
#     payload = {
#         "jsonrpc": "2.0",
#         "method": "subtract",
#         "params": [42, 23],
#         "id": "1"
#     }
#     response = client.post('/api/', json=payload).json()
#     assert response['jsonrpc'] == '2.0'
#     assert response['id'] == 1
#     assert response['result'] == 19


# def test_server_must_response_with_result_when_ok():
#     payload = {
#         "jsonrpc": "2.0",
#         "method": "my_method",
#         "params": {},
#         "id": "1"
#     }
#     response = client.post('/api/', json=payload).json()
#     assert response['jsonrpc'] == '2.0'
#     assert response['id'] == '1'
#     assert response['result'] == {'test': 'method'}
#
#
# def test_server_must_response_with_error_when_not_ok():
#     payload = {
#         "jsonrpc": "2.0",
#         "method": "my_method",
#         "params": {},
#         "id": "1"
#     }
#     response = client.post('/api/', json=payload).json()
#     assert response['jsonrpc'] == '2.0'
#     assert response['id'] == '1'
#     assert response['error'] == {
#         'code': '',
#         'message': '',
#         'data': ''
#     }
