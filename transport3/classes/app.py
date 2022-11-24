from .simulation import Simulation
from .simulation_app_ui import SimulationAppUI


class App:
    def __init__(self):
        self.simulation = Simulation()
        self.simulation_app_ui = SimulationAppUI(self.simulation)

    def run(self):
        self.simulation_app_ui.run()
