import types

from starlette_jsonrpc import dispatcher


def test_adding_methods_to_dispatcher():
    func = dispatcher.methods_map.get("subtract")
    assert func is not None
    assert isinstance(func, types.FunctionType) is True

    func = dispatcher.methods_map.get("SubtractMethod")
    assert func is not None
    assert isinstance(func, types.FunctionType) is True

    func = dispatcher.methods_map.get("subtract_positional")
    assert func is not None
    assert isinstance(func, types.FunctionType) is True
