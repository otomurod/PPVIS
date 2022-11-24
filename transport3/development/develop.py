class Switch:
    def __init__(self, name, station1, station2):
        self.name = name
        self.station1 = station1
        self.station2 = station2
        self.route1 = []
        self.route2 = []
        self.route = self.route1
        self.route_index = 0
        self.next_station = None

    def set_route1(self, route):
        self.route1 = route
        self.next_station = route[0]

    def set_route2(self, route):
        self.route2 = route
        self.next_station = route[0]

    def move(self):
        if self.next_station is not None:
            self.station1.remove_train()
            self.station1 = self.next_station
            self.station1.add_train(self)
            self.route_index += 1
            if self.route_index < len(self.route):
                self.next_station = self.route[self.route_index]
            else:
                self.next_station = None
