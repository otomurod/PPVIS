class Train:
    def __init__(self, name, station):
        self.name = name
        self.station = station
        self.passengers = []
        self.goods = []
        self.speed = 0
        self.route = []
        self.route_index = 0
        self.next_station = None
        self.wagons = []
        self.locomotive = None

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def add_goods(self, goods):
        self.goods.append(goods)

    def remove_passenger(self, passenger):
        self.passengers.remove(passenger)

    def remove_goods(self, goods):
        self.goods.remove(goods)

    def set_route(self, route):
        self.route = route
        self.next_station = route[0]

    def move(self):
        if self.next_station is not None:
            print(
                f'Поезд {self.name} прибыл на станцию {self.next_station.name}')
            self.station.remove_train()
            self.station = self.next_station
            self.station.add_train(self)
            self.route_index += 1
            # посадка пассажиров
            for passenger in self.passengers:
                if passenger.station == self.station:
                    self.station.add_passenger(passenger)
                    self.remove_passenger(passenger)
                    print(
                        f'Пассажир {passenger.name} сел в поезд {self.name} на станции {self.station.name}')
            # высадка пассажиров
            for passenger in self.station.passengers:
                if passenger.station == self.station:
                    self.add_passenger(passenger)
                    self.station.remove_passenger(passenger)
                    print(
                        f'Пассажир {passenger.name} вышел из поезда {self.name} на станции {self.station.name}')
            # погрузка товаров
            for goods in self.goods:
                if goods.station == self.station:
                    self.station.add_goods(goods)
                    self.remove_goods(goods)
                    print(
                        f'Товар {goods.name} погружен в поезд {self.name} на станции {self.station.name}')
            # разгрузка товаров
            for goods in self.station.goods:
                if goods.station == self.station:
                    self.add_goods(goods)
                    self.station.remove_goods(goods)
                    print(
                        f'Товар {goods.name} разгружен из поезда {self.name} на станции {self.station.name}')
            # загрузка товаров
            for goods in self.station.goods:
                if goods.station == self.next_station:
                    self.next_station.add_goods(goods)
                    self.station.remove_goods(goods)
                    print(
                        f'Товар {goods.name} загружен в поезд {self.name} на станции {self.station.name}')
            # выгрузка товаров
            for goods in self.goods:
                if goods.station == self.next_station:
                    self.next_station.add_goods(goods)
                    self.remove_goods(goods)
                    print(
                        f'Товар {goods.name} выгружен из поезда {self.name} на станции {self.station.name}')
            if self.route_index < len(self.route):
                self.next_station = self.route[self.route_index]
                print(
                    f'Поезд {self.name} отправляется со станции {self.station.name} на станцию {self.next_station.name}')
            else:
                self.next_station = None
                print(
                    f'Поезд {self.name} прибыл в конечную станцию {self.station.name}')
            if self.route_index < len(self.route):
                self.next_station = self.route[self.route_index]
            else:
                self.next_station = None
                print(
                    f'Поезд {self.name} прибыл в конечную станцию {self.station.name}')

    def add_wagon(self, wagon):
        self.wagons.append(wagon)

    def remove_wagon(self, wagon):
        self.wagons.remove(wagon)

    def add_locomotive(self, locomotive):
        self.locomotive = locomotive

    def remove_locomotive(self):
        self.locomotive = None

    def add_passenger_to_wagon(self, passenger, wagon):
        if passenger in self.passengers:
            wagon.add_passenger(passenger)
            self.passengers.remove(passenger)

    def remove_passenger_from_wagon(self, passenger, wagon):
        if passenger in wagon.passengers:
            self.passengers.append(passenger)
            wagon.passengers.remove(passenger)

    def add_goods_to_wagon(self, goods, wagon):
        if goods in self.goods:
            wagon.add_goods(goods)
            self.goods.remove(goods)

    def remove_goods_from_wagon(self, goods, wagon):
        if goods in wagon.goods:
            self.goods.append(goods)
            wagon.goods.remove(goods)

    def set_speed(self, speed):
        self.speed = speed

    def switch_to_other_path(self, path):
        self.path = path

    def load_goods_to_station(self, goods, station):
        if goods in self.goods:
            station.add_goods(goods)
            self.goods.remove(goods)

    def unload_goods_from_station(self, goods, station):
        if goods in station.goods:
            self.goods.append(goods)
            station.goods.remove(goods)

    def load_goods_to_wagon(self, goods, wagon):
        if goods in self.goods:
            wagon.add_goods(goods)
            self.goods.remove(goods)

    def unload_goods_from_wagon(self, goods, wagon):
        if goods in wagon.goods:
            self.goods.append(goods)
            wagon.goods.remove(goods)

    def load_passenger_to_station(self, passenger, station):
        if passenger in self.passengers:
            station.add_passenger(passenger)
            self.passengers.remove(passenger)

    def unload_passenger_from_station(self, passenger, station):
        if passenger in station.passengers:
            self.passengers.append(passenger)
            station.passengers.remove(passenger)

    def load_passenger_to_wagon(self, passenger, wagon):
        if passenger in self.passengers:
            wagon.add_passenger(passenger)
            self.passengers.remove(passenger)

    def unload_passenger_from_wagon(self, passenger, wagon):
        if passenger in wagon.passengers:
            self.passengers.append(passenger)
            wagon.passengers.remove(passenger)

    def run(self):
        while self.next_station is not None:
            self.move()

    def __str__(self):
        return f'Поезд {self.name}'
