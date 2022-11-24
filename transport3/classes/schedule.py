from .graph import Graph


class Schedule:
    def __init__(self, train, time, station, path):
        self.train = train
        self.time = time
        self.station = station
        self.path = Graph(path, self.train.route).get_route()

    def run(self):
        self.train.add_station(self.station)
        self.train.add_path(self.path)
        self.train.run()
