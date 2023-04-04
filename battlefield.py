from robot import Robot
from dinosaur import Dinosaur


class Battlefield:
    def __init__(self) -> None:
        self.robot = Robot("Bob")
        self.dinosaur = Dinosaur("Littlefoot", 20)

    def run_game(self):
        pass

    def display_welcome(self):
        pass

    def battle_phase(self):
        pass

    def display_winner(self):
        pass
