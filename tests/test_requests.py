from . import client


def test_post_call_should_return_status_code_200():
    payload = {
        "jsonrpc": "2.0",
        "method": "substract",
        "params": {},
        "id": "1"
    }
    response = client.post('/api/', json=payload)
    assert response.status_code == 200


def test_post_for_named_function_should_return_status_code_200():
    payload = {
        "jsonrpc": "2.0",
        "method": "SubstractMethod",
        "params": {},
        "id": '1'
    }
    response = client.post('/api/', json=payload)
    assert response.status_code == 200


def test_get_call_should_return_method_not_allowed():
    response = client.get('/api/')
    assert response.status_code == 405


def test_put_call_should_return_method_not_allowed():
    payload = {
        "jsonrpc": "2.0",
        "method": "substract",
        "params": {},
        "id": "1"
    }
    response = client.put('/api/', data=payload)
    assert response.status_code == 405


def test_delete_call_should_return_method_not_allowed():
    response = client.delete('/api/')
    assert response.status_code == 405


def test_patch_call_should_return_method_not_allowed():
    payload = {
        "jsonrpc": "2.0",
        "method": "substract",
        "params": {},
        "id": "1"
    }
    response = client.patch('/api/', payload)
    assert response.status_code == 405


def test_with_not_registered_method_should_return_method_not_found():
    payload = {
        "jsonrpc": "2.0",
        "method": "non_existing_method",
        "params": {},
        "id": "1"
    }
    response = client.post('/api/', json=payload)
    assert response.json() == {
        "jsonrpc": "2.0",
        "id": "1",
        "error": {
            "code": -32601,
            "message": "Method not found.",
            "data": {}
        }
    }


def test_with_id_as_string_should_return_invalid_params_exception():
    payload = {
        "jsonrpc": "2.0",
        "method": "substract",
        "params": {},
        "id": 1
    }
    response = client.post('/api/', json=payload)
    assert response.json() == {
        "jsonrpc": "2.0",
        "id": "1",
        "error": {
            "code": -32602,
            "message": "Invalid params.",
            "data": {
                "id": "Must be a string."
            }
        }
    }
