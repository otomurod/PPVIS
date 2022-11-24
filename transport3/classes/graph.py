class Graph:
    def __init__(self, path, route):
        self.path = path
        self.route = route

    def add_train(self, train):
        self.train = train

    def remove_train(self):
        self.train = None

    def get_route(self):
        return self.path

    def __str__(self) -> str:
        return f'График движения поезда {self.path}'
