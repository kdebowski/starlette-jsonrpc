import functools


class Dispatcher:
    def __init__(self):
        self.routes_map = {}

    def add_method(self, method=None, name=None):

        if name and not method:
            return functools.partial(self.add_method, name=name)

        self.routes_map[name or method.__name__] = method
        return method
