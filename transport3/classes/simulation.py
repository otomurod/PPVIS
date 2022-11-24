class Simulation:
    def __init__(self):
        self.stations = []
        self.trains = []
        self.schedules = []
        self.goods = []
        self.wagons = []
        self.locomotives = []

    def add_station(self, station):
        self.stations.append(station)

    def add_train(self, train):
        self.trains.append(train)

    def add_schedule(self, schedule):
        self.schedules.append(schedule)

    def add_passenger_to_station(self, passenger, station):
        station.add_passenger(passenger)

    def add_passenger_to_train(self, passenger, train):
        train.add_passenger(passenger)

    def add_goods_to_station(self, goods, station):
        station.add_goods(goods)

    def add_goods_to_train(self, goods, train):
        train.add_goods(goods)

    def add_wagon_to_train(self, wagon, train):
        train.add_wagon(wagon)

    def add_locomotive_to_train(self, locomotive, train):
        train.add_locomotive(locomotive)

    def remove_station(self, station):
        self.stations.remove(station)

    def remove_train(self, train):
        self.trains.remove(train)

    def remove_schedule(self, schedule):
        self.schedules.remove(schedule)

    def remove_passenger_from_station(self, passenger, station):
        station.remove_passenger(passenger)

    def remove_passenger_from_train(self, passenger, train):
        train.remove_passenger(passenger)

    def remove_goods_from_station(self, goods, station):
        station.remove_goods(goods)

    def remove_goods_from_train(self, goods, train):
        train.remove_goods(goods)

    def remove_wagon_from_train(self, wagon, train):
        train.remove_wagon(wagon)

    def remove_locomotive_from_train(self, locomotive, train):
        train.remove_locomotive(locomotive)

    def switch_to_other_path(self, path, train):
        train.switch_to_other_path(path)

    def set_speed(self, speed, train):
        train.set_speed(speed)

    def show_speed(self, train):
        print(train.name, train.speed, 'км/ч')

    def get_station_by_name(self, name):
        for station in self.stations:
            if station.name == name:
                return station
        return None

    def get_train_by_name(self, name):
        for train in self.trains:
            if train.name == name:
                return train
        return None

    def all_stations(self):
        return self.stations

    def show_schedule(self):
        for schedule in self.schedules:
            print(schedule.train.name, schedule.path, schedule.time)

    def __str__(self):
        return 'Simulation'

    def __repr__(self):
        return 'Simulation'

    def run(self):
        # train movement with schedule
        # train movement without schedule
        for train in self.trains:
            train.move()
