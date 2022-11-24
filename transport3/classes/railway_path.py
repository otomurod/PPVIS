class RailwayPath:
    def __init__(self, name):
        self.name = name
        self.train = None

    def add_train(self, train):
        self.train = train

    def remove_train(self):
        self.train = None
