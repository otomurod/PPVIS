class Goods:
    def __init__(self, name, station):
        self.name = name
        self.station = station

    def __str__(self):
        return f'Груз {self.name}'