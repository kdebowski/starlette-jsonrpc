from . import client


# JSON


def test_payload_as_empty_dict():
    payload = {}
    response = client.post("/api/", json=payload)
    assert response.json() == {
        "jsonrpc": "2.0",
        "id": "None",
        "error": {"code": -32602, "message": "Invalid params.", "data": {}},
    }


def test_payload_as_empty_list():
    payload = []
    response = client.post("/api/", json=payload)
    assert response.json() == {
        "jsonrpc": "2.0",
        "id": "None",
        "error": {"code": -32602, "message": "Invalid params.", "data": {}},
    }


def test_incorrect_payload():
    payload = [1]
    response = client.post("/api/", json=payload)
    assert response.json() == {
        "jsonrpc": "2.0",
        "id": "None",
        "error": {"code": -32602, "message": "Invalid params.", "data": {}},
    }


# PARAMS


def test_positional_parameters():
    payload = {
        "jsonrpc": "2.0",
        "method": "subtract_positional",
        "params": [42, 23],
        "id": "1",
    }
    response = client.post("/api/", json=payload)
    assert response.json() == {"jsonrpc": "2.0", "id": "1", "result": 19}


def test_named_parameters():
    payload = {
        "jsonrpc": "2.0",
        "method": "SubtractMethod",
        "params": {"x": 42, "y": 23},
        "id": "1",
    }
    response = client.post("/api/", json=payload)
    assert response.json() == {"jsonrpc": "2.0", "id": "1", "result": 19}


def test_named_parameters_2():
    payload = {
        "jsonrpc": "2.0",
        "method": "sum",
        "params": {"x": 42, "y": 23},
        "id": "1",
    }
    response = client.post("/api/", json=payload)
    assert response.json() == {"jsonrpc": "2.0", "id": "1", "result": {"sum": 65}}


def test_params_not_object():
    payload = {"jsonrpc": "2.0", "method": "subtract", "params": "", "id": "1"}
    response = client.post("/api/", json=payload)
    assert response.json() == {
        "jsonrpc": "2.0",
        "id": "1",
        "error": {
            "code": -32602,
            "message": "Invalid params.",
            "data": {"params": "Did not match any valid type."},
        },
    }


def test_params_as_invalid_object():
    payload = {"jsonrpc": "2.0", "method": "subtract", "params": {}, "id": "1"}
    response = client.post("/api/", json=payload)
    assert response.json() == {
        "jsonrpc": "2.0",
        "id": "1",
        "error": {
            "code": -32602,
            "message": "Invalid params.",
            "data": {"params": "Required param: 'x'"},
        },
    }


def test_params_as_invalid_list():
    payload = {
        "jsonrpc": "2.0",
        "method": "subtract_positional",
        "params": [1],
        "id": "1",
    }
    response = client.post("/api/", json=payload)
    assert response.json() == {
        "jsonrpc": "2.0",
        "id": "1",
        "error": {
            "code": -32602,
            "message": "Invalid params.",
            "data": {
                "params": "subtract_positional() missing 1 required positional argument: 'y'"
            },
        },
    }


def test_without_params():
    payload = {"jsonrpc": "2.0", "method": "my_method", "id": "1"}
    response = client.post("/api/", json=payload)
    assert response.status_code == 200


# ID


def test_id_as_integer():
    payload = {
        "jsonrpc": "2.0",
        "method": "subtract",
        "params": {"x": 42, "y": 23},
        "id": 1,
    }
    response = client.post("/api/", json=payload)
    assert response.json() == {"jsonrpc": "2.0", "id": 1, "result": 19}


def test_id_as_string():
    payload = {
        "jsonrpc": "2.0",
        "method": "subtract",
        "params": {"x": 42, "y": 23},
        "id": "abc",
    }
    response = client.post("/api/", json=payload)
    assert response.json() == {"jsonrpc": "2.0", "id": "abc", "result": 19}


def test_id_as_null():
    payload = {
        "jsonrpc": "2.0",
        "method": "subtract",
        "params": {"x": 42, "y": 23},
        "id": None,
    }
    response = client.post("/api/", json=payload)
    assert response.json() == {"jsonrpc": "2.0", "id": None, "result": 19}


def test_empty_id():
    payload = {
        "jsonrpc": "2.0",
        "method": "subtract",
        "params": {"x": 42, "y": 23},
        "id": "",
    }
    response = client.post("/api/", json=payload)
    assert response.json() == {"jsonrpc": "2.0", "id": None, "result": 19}


def test_without_id():
    """
    Notification
    """
    payload = {"jsonrpc": "2.0", "method": "subtract", "params": {"x": 42, "y": 23}}
    response = client.post("/api/", json=payload)
    assert response.json() == {}


# JSONRPC


def test_jsonrpc_as_integer():
    payload = {
        "jsonrpc": 2,
        "method": "subtract",
        "params": {"x": 42, "y": 23},
        "id": "1",
    }
    response = client.post("/api/", json=payload)
    assert response.json() == {
        "jsonrpc": "2.0",
        "id": "1",
        "error": {
            "code": -32602,
            "message": "Invalid params.",
            "data": {"jsonrpc": "Must be a string."},
        },
    }


def test_empty_jsonrpc():
    payload = {
        "jsonrpc": "",
        "method": "subtract",
        "params": {"x": 42, "y": 23},
        "id": "1",
    }
    response = client.post("/api/", json=payload)
    assert response.json() == {
        "jsonrpc": "2.0",
        "id": "1",
        "error": {
            "code": -32602,
            "message": "Invalid params.",
            "data": {"jsonrpc": "Must not be blank."},
        },
    }


def test_jsonrpc_wrong_value():
    payload = {
        "jsonrpc": "3.0",
        "method": "subtract",
        "params": {"x": 42, "y": 23},
        "id": "1",
    }
    response = client.post("/api/", json=payload)
    assert response.json() == {
        "jsonrpc": "2.0",
        "id": "1",
        "error": {
            "code": -32602,
            "message": "Invalid params.",
            "data": {"jsonrpc": "Must match the pattern /2.0/."},
        },
    }


def test_without_jsonrpc():
    payload = {"method": "subtract", "params": {"x": 42, "y": 23}, "id": "1"}
    response = client.post("/api/", json=payload)
    assert response.json() == {
        "jsonrpc": "2.0",
        "id": "1",
        "error": {
            "code": -32602,
            "message": "Invalid params.",
            "data": {"jsonrpc": "This field is required."},
        },
    }


# METHOD


def test_not_registered_method():
    payload = {
        "jsonrpc": "2.0",
        "method": "non_existing_method",
        "params": {"x": 42, "y": 23},
        "id": "1",
    }
    response = client.post("/api/", json=payload)
    assert response.json() == {
        "jsonrpc": "2.0",
        "id": "1",
        "error": {"code": -32601, "message": "Method not found.", "data": {}},
    }


def test_without_method():
    payload = {"jsonrpc": "2.0", "params": {"x": 42, "y": 23}, "id": "1"}
    response = client.post("/api/", json=payload)
    assert response.json() == {
        "jsonrpc": "2.0",
        "id": "1",
        "error": {
            "code": -32602,
            "message": "Invalid params.",
            "data": {"method": "This field is required."},
        },
    }


def test_with_empty_method():
    payload = {"jsonrpc": "2.0", "method": "", "params": {"x": 42, "y": 23}, "id": "1"}
    response = client.post("/api/", json=payload)
    assert response.json() == {
        "jsonrpc": "2.0",
        "id": "1",
        "error": {
            "code": -32602,
            "message": "Invalid params.",
            "data": {"method": "Must not be blank."},
        },
    }


def test_method_as_integer():
    payload = {"jsonrpc": "2.0", "method": 1, "params": {"x": 42, "y": 23}, "id": "1"}
    response = client.post("/api/", json=payload)
    assert response.json() == {
        "jsonrpc": "2.0",
        "id": "1",
        "error": {
            "code": -32602,
            "message": "Invalid params.",
            "data": {"method": "Must be a string."},
        },
    }


# def test_with_method_name_starting_with_rpc_period():
#     pass
