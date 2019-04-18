import functools


class Dispatcher:
    def __init__(self):
        self.methods_map = {}

    def add_method(self, method: str = None, name: str = None):

        if name and not method:
            return functools.partial(self.add_method, name=name)

        self.methods_map[name or method.__name__] = method
        return method
