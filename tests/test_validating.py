from . import client


def test_with_params_not_being_object_should_return_invalid_params_exception():
    payload = {
        "jsonrpc": "2.0",
        "method": "substract",
        "params": [],
        "id": "1"
    }
    response = client.post('/api/', json=payload)
    assert response.json() == {
        "jsonrpc": "2.0",
        "id": "1",
        "error": {
            "code": -32602,
            "message": "Invalid params.",
            "data": {
                "params": "Must be an object."
            }
        }
    }


def test_request_without_jsonrpc_parameter_should_return_():
    payload = {
        "method": "substract",
        "params": {},
        "id": "1"
    }
    response = client.post('/api/', json=payload)
    assert response.json() == {
        "jsonrpc": "2.0",
        "id": "1",
        "error": {
            "code": -32602,
            "message": "Invalid params.",
            "data": {
                "jsonrpc": "This field is required."
            }
        }
    }

# def test_request_without_params_returns_200():
#     payload = {
#         "jsonrpc": "2.0",
#         "method": "my_method",
#         "id": "1"
#     }
#     response = client.post('/api/', json=payload)
#     assert response.status_code == 200
#
#
# def test_with_wrong_value_of_jsonrpc():
#     pass
#
#
# def test_without_jsonrpc():
#     pass
#
#
# def test_without_method():
#     pass
#
#
# def test_id_must_be_string():
#     pass
#


# def test_with_method_name_starting_with_rpc_period():
#     pass
#
#
# def test_without_id():
#     pass
#
#
# def test_with_empty_id():
#     pass
#
#
# def test_without_params_ok():
#     pass