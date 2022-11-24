class Station:
    def __init__(self, name):
        self.name = name
        self.passengers = []
        self.goods = []
        self.train = None

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def add_goods(self, goods):
        self.goods.append(goods)

    def add_train(self, train):
        self.train = train

    def remove_train(self):
        self.train = None

    def remove_passenger(self, passenger):
        self.passengers.remove(passenger)

    def remove_goods(self, goods):
        self.goods.remove(goods)

    def __str__(self):
        return f'Станция {self.name}'
