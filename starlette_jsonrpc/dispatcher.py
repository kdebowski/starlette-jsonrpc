class Dispatcher:

    def __init__(self):
        self.routes_map = {}

    def add_method(self, method, name=None):
        method_name = name if name else method.__name__
        self.routes_map[method_name] = method
        return method
