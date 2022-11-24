class Locomotive:
    def __init__(self, name, train):
        self.name = name
        self.train = train

    def __str__(self):
        return f'Локомотив {self.name}'
