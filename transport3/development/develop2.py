from tkinter import *


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
        return self.name

    def __repr__(self):
        return self.name


class Passenger:
    def __init__(self, name, station):
        self.name = name
        self.station = station

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Goods:
    def __init__(self, name, station):
        self.name = name
        self.station = station

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class RailwayCrossing:
    def __init__(self, name):
        self.name = name
        self.train = None

    def add_train(self, train):
        self.train = train

    def remove_train(self):
        self.train = None

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Semaphore:
    def __init__(self, name):
        self.name = name
        self.train = None

    def add_train(self, train):
        self.train = train

    def remove_train(self):
        self.train = None

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class RailwayPath:
    def __init__(self, name):
        self.name = name
        self.train = None

    def add_train(self, train):
        self.train = train

    def remove_train(self):
        self.train = None

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Schedule:
    def __init__(self, name):
        self.name = name
        self.trains = []

    def add_train(self, train):
        self.trains.append(train)

    def remove_train(self, train):
        self.trains.remove(train)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Locomotive:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Wagon:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

# посадка в вагоны, высадка пассажиров, скорость поезда, погрузка товаров в вагон, разгрузка товаров из вагона на склад, склад товаров на станции


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
            self.station.remove_train()
            self.station = self.next_station
            self.station.add_train(self)
            self.route_index += 1
            if self.route_index < len(self.route):
                self.next_station = self.route[self.route_index]
            else:
                self.next_station = None

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

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

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
        return self.name

    def switch_route(self):
        if self.route == self.route1:
            self.route = self.route2
            self.next_station = self.route[0]
        else:
            self.route = self.route1
            self.next_station = self.route[0]


class Simulation:
    def __init__(self):
        self.stations = []
        self.trains = []
        self.schedules = []
        self.passengers = []
        self.goods = []
        self.wagons = []
        self.locomotives = []

    def add_station(self, station):
        self.stations.append(station)

    def add_train(self, train):
        self.trains.append(train)

    def add_schedule(self, schedule):
        self.schedules.append(schedule)

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def add_goods(self, goods):
        self.goods.append(goods)

    def add_wagon(self, wagon):
        self.wagons.append(wagon)

    def add_locomotive(self, locomotive):
        self.locomotives.append(locomotive)

    def remove_station(self, station):
        self.stations.remove(station)

    def remove_train(self, train):
        self.trains.remove(train)

    def remove_schedule(self, schedule):
        self.schedules.remove(schedule)

    def remove_passenger(self, passenger):
        self.passengers.remove(passenger)

    def remove_goods(self, goods):
        self.goods.remove(goods)

    def remove_wagon(self, wagon):
        self.wagons.remove(wagon)

    def remove_locomotive(self, locomotive):
        self.locomotives.remove(locomotive)

    def __str__(self):
        return 'Simulation'

    def __repr__(self):
        return 'Simulation'

    def run(self):
        for train in self.trains:
            if train.next_station is not None:
                train.move()


class SimulationApp:
    def __init__(self):
        self.simulation = Simulation()

    def run(self):
        self.simulation.run()

    def add_station(self, name):
        self.simulation.add_station(Station(name))

    def add_train(self, name):
        self.simulation.add_train(Train(name))

    def add_schedule(self, train, route):
        self.simulation.add_schedule(Schedule(train, route))

    def add_passenger(self, name):
        self.simulation.add_passenger(Passenger(name))

    def add_goods(self, name):
        self.simulation.add_goods(Goods(name))

    def add_wagon(self, name):
        self.simulation.add_wagon(Wagon(name))

    def add_locomotive(self, name):
        self.simulation.add_locomotive(Locomotive(name))

    def remove_station(self, station):
        self.simulation.remove_station(station)

    def remove_train(self, train):
        self.simulation.remove_train(train)

    def remove_schedule(self, schedule):
        self.simulation.remove_schedule(schedule)

    def remove_passenger(self, passenger):
        self.simulation.remove_passenger(passenger)

    def remove_goods(self, goods):
        self.simulation.remove_goods(goods)

    def remove_wagon(self, wagon):
        self.simulation.remove_wagon(wagon)

    def remove_locomotive(self, locomotive):
        self.simulation.remove_locomotive(locomotive)

    def get_stations(self):
        return self.simulation.stations

    def get_trains(self):
        return self.simulation.trains

    def get_schedules(self):
        return self.simulation.schedules

    def get_passengers(self):
        return self.simulation.passengers

    def get_goods(self):
        return self.simulation.goods

    def get_wagons(self):
        return self.simulation.wagons

    def get_locomotives(self):
        return self.simulation.locomotives

    def get_station(self, name):
        for station in self.simulation.stations:
            if station.name == name:
                return station

    def get_train(self, name):
        for train in self.simulation.trains:
            if train.name == name:
                return train

    def get_schedule(self, name):
        for schedule in self.simulation.schedules:
            if schedule.name == name:
                return schedule

    def get_passenger(self, name):
        for passenger in self.simulation.passengers:
            if passenger.name == name:
                return passenger
# Create user interface for simulation app in console


class SimulationAppUI:
    def __init__(self):
        self.simulation_app = SimulationApp()

    def run(self):
        self.simulation_app.run()

    def add_station(self):
        name = input('Enter station name: ')
        self.simulation_app.add_station(name)

    def add_train(self):
        name = input('Enter train name: ')
        self.simulation_app.add_train(name)

    def add_schedule(self):
        train = self.get_train()
        route = self.get_route()
        self.simulation_app.add_schedule(train, route)

    def add_passenger(self):
        name = input('Enter passenger name: ')
        self.simulation_app.add_passenger(name)

    def add_goods(self):
        name = input('Enter goods name: ')
        self.simulation_app.add_goods(name)

    def add_wagon(self):
        name = input('Enter wagon name: ')
        self.simulation_app.add_wagon(name)

    def add_locomotive(self):
        name = input('Enter locomotive name: ')
        self.simulation_app.add_locomotive(name)

    def remove_station(self):
        station = self.get_station()
        self.simulation_app.remove_station(station)

    def remove_train(self):
        train = self.get_train()
        self.simulation_app.remove_train(train)

    def remove_schedule(self):
        schedule = self.get_schedule()
        self.simulation_app.remove_schedule(schedule)

    def remove_passenger(self):
        passenger = self.get_passenger()
        self.simulation_app.remove_passenger(passenger)

    def remove_goods(self):
        goods = self.get_goods()
        self.simulation_app.remove_goods(goods)

    def remove_wagon(self):
        wagon = self.get_wagon()
        self.simulation_app.remove_wagon(wagon)

    def remove_locomotive(self):
        locomotive = self.get_locomotive()
        self.simulation_app.remove_locomotive(locomotive)

    def get_stations(self):
        return self.simulation_app.get_stations()

    def get_trains(self):
        return self.simulation_app.get_trains()

    def get_schedules(self):
        return self.simulation_app.get_schedules()

    def get_passengers(self):
        return self.simulation_app.get_passengers()

    def get_goods(self):
        return self.simulation_app.get_goods()

    def get_wagons(self):
        return self.simulation_app.get_wagons()

    def get_locomotives(self):
        return self.simulation_app.get_locomotives()

    def get_station(self):
        name = input('Enter station name: ')
        return self.simulation_app.get_station(name)

    def get_train(self):
        name = input('Enter train name: ')
        return self.simulation_app.get_train(name)

    def get_schedule(self):
        name = input('Enter schedule name: ')
        return self.simulation_app.get_schedule(name)

    def get_passenger(self):
        name = input('Enter passenger name: ')
        return self.simulation_app.get_passenger(name)


class App:
    def __init__(self):
        self.simulation = Simulation()
        self.ui = SimulationAppUI()

    def run(self):
        while True:
            print('1. Add station')
            print('2. Add train')
            print('3. Add schedule')
            print('4. Add passenger')
            print('5. Add goods')
            print('6. Add wagon')
            print('7. Add locomotive')
            print('8. Remove station')
            print('9. Remove train')
            print('10. Remove schedule')
            print('11. Remove passenger')
            print('12. Remove goods')
            print('13. Remove wagon')
            print('14. Remove locomotive')
            print('15. Get stations')
            print('16. Get trains')
            print('17. Get schedules')
            print('18. Get passengers')
            print('19. Get goods')
            print('20. Get wagons')
            print('21. Get locomotives')
            print('22. Get station')
            print('23. Get train')
            print('24. Get schedule')
            print('25. Get passenger')
            print('26. Get goods')
            print('27. Get wagon')
            print('28. Get locomotive')
            print('29. Run simulation')
            print('30. Exit')
            choice = int(input('Enter choice: '))
            if choice == 1:
                self.ui.add_station()
            elif choice == 2:
                self.ui.add_train()
            elif choice == 3:
                self.ui.add_schedule()
            elif choice == 4:
                self.ui.add_passenger()
            elif choice == 5:
                self.ui.add_goods()
            elif choice == 6:
                self.ui.add_wagon()
            elif choice == 7:
                self.ui.add_locomotive()
            elif choice == 8:
                self.ui.remove_station()
            elif choice == 9:
                self.ui.remove_train()
            elif choice == 10:
                self.ui.remove_schedule()
            elif choice == 11:
                self.ui.remove_passenger()
            elif choice == 12:
                self.ui.remove_goods()
            elif choice == 13:
                self.ui.remove_wagon()
            elif choice == 14:
                self.ui.remove_locomotive()
            elif choice == 15:
                stations = self.ui.get_stations()
                for station in stations:
                    print(station)
            elif choice == 16:
                trains = self.ui.get_trains()
                for train in trains:
                    print(train)
            elif choice == 17:
                schedules = self.ui.get_schedules()
                for schedule in schedules:
                    print(schedule)
            elif choice == 18:
                passengers = self.ui.get_passengers()
                for passenger in passengers:
                    print(passenger)
            elif choice == 19:
                goods = self.ui.get_goods()
                for good in goods:
                    print(good)
            elif choice == 20:
                wagons = self.ui.get_wagons()
                for wagon in wagons:
                    print(wagon)
            elif choice == 21:
                locomotives = self.ui.get_locomotives()
                for locomotive in locomotives:
                    print(locomotive)
            elif choice == 22:
                station = self.ui.get_station()
                print(station)
            elif choice == 23:
                train = self.ui.get_train()
                print(train)
            elif choice == 24:
                schedule = self.ui.get_schedule()
                print(schedule)
            elif choice == 25:
                passenger = self.ui.get_passenger()
                print(passenger)
            elif choice == 26:
                good = self.ui.get_good()
                print(good)
            elif choice == 27:
                wagon = self.ui.get_wagon()
                print(wagon)
            elif choice == 28:
                locomotive = self.ui.get_locomotive()
                print(locomotive)
            elif choice == 29:
                self.simulation.run()
            elif choice == 30:
                break


if __name__ == '__main__':
    app = App()
    app.run()
