from weapon import Weapon


class Robot:
    def __init__(self, name) -> None:
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("Battle Axe", 20)

    def attack(self, dinosaur):
        pass
