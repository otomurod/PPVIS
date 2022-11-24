from .locomotive import Locomotive
from .passenger import Passenger
from .products import Goods
from .schedule import Schedule
from .station import Station
from .train import Train
from .wagon import Wagon


class SimulationAppUI:
    def __init__(self, simulation):
        self.simulation = simulation

    def run(self):
        while True:
            print('1. Add station')
            print('2. Add train')
            print('3. Add schedule')
            print('4. Add passenger to station')
            print('5. Add passenger to train')
            print('6. Add goods to station')
            print('7. Add goods to train')
            print('8. Add wagon to train')
            print('9. Add locomotive to train')
            print('10. Show schedule')
            print('11. Set speed')
            print('12. Show speed')
            print('13. Switch to other path')
            print('14. Run simulation')
            print('0. Exit')

            choice = input('Enter your choice: ')
            if choice == '1':
                name = input('Enter station name: ')
                station = Station(name)
                self.simulation.add_station(station)
            elif choice == '2':
                name = input('Enter train name: ')
                station_name = input('Enter station name: ')
                station = self.simulation.get_station_by_name(station_name)
                train = Train(name, station)
                self.simulation.add_train(train)
            elif choice == '3':
                train_name = input('Enter train name: ')
                train = self.simulation.get_train_by_name(train_name)

                if train is not None:
                    route = []
                    while True:
                        station_name = input('Enter station name: ')
                        station = self.simulation.get_station_by_name(
                            station_name)
                        time = input('Enter time: ')
                        if station is not None:
                            route.append(station)
                        else:
                            print('Station not found')
                        if input('Add another station? (y/n): ') == 'n':
                            break
                        add_train_schedule = Schedule(
                            train, time, station, route)

                        self.simulation.add_schedule(add_train_schedule)
                    train.set_route(route)
                else:
                    print('Train not found')
            elif choice == '4':
                name = input('Enter passenger name: ')
                station_name = input('Enter station name: ')
                station = self.simulation.get_station_by_name(station_name)
                passenger = Passenger(name, station)
                self.simulation.add_passenger_to_station(passenger, station)
            elif choice == '5':
                name = input('Enter passenger name: ')
                train_name = input('Enter train name: ')
                train = self.simulation.get_train_by_name(train_name)
                station_name = input('Enter station name: ')
                station = self.simulation.get_station_by_name(station_name)
                passenger = Passenger(name, station)
                self.simulation.add_passenger_to_train(passenger, train)
            elif choice == '6':
                name = input('Enter goods name: ')
                station_name = input('Enter station name: ')
                station = self.simulation.get_station_by_name(station_name)
                goods = Goods(name, station)
                self.simulation.add_goods_to_station(goods, station)
            elif choice == '7':
                name = input('Enter goods name: ')
                train_name = input('Enter train name: ')
                station_name = input('Enter station name: ')
                train = self.simulation.get_train_by_name(train_name)
                station = self.simulation.get_station_by_name(station_name)
                goods = Goods(name, station)
                self.simulation.add_goods_to_train(goods, train)
            elif choice == '8':
                name = input('Enter wagon name: ')
                train_name = input('Enter train name: ')
                train = self.simulation.get_train_by_name(train_name)
                wagon = Wagon(name, train)
                self.simulation.add_wagon_to_train(wagon, train)
            elif choice == '9':
                name = input('Enter locomotive name: ')
                train_name = input('Enter train name: ')
                train = self.simulation.get_train_by_name(train_name)
                locomotive = Locomotive(name, train)
                self.simulation.add_locomotive_to_train(locomotive, train)
            elif choice == '10':
                self.simulation.show_schedule()
            elif choice == '11':
                speed = input('Enter speed: ')
                train_name = input('Enter train name: ')
                train = self.simulation.get_train_by_name(train_name)
                self.simulation.set_speed(speed, train)
            elif choice == '12':
                train_name = input('Enter train name: ')
                train = self.simulation.get_train_by_name(train_name)
                self.simulation.show_speed(train)
            elif choice == '13':
                # change path of the train and schedule to other
                train_name = input('Enter train name: ')
                train = self.simulation.get_train_by_name(train_name)
                # print all available stations
                self.simulation.all_stations()
                path = input('Enter path: ')
                self.simulation.switch_to_other_path(path, train)

            elif choice == '14':
                self.simulation.run()
            elif choice == '0':
                break
