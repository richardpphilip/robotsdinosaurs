import weapon


class Robot:
    def __init__(self, robot_name='beast', robot_attack_power=2):
        self.robot_name = robot_name
        self.robot_health = 100
        self.robot_energy = 10
        self.robot_attack_power = robot_attack_power

    def robot_attack_power(self, weapon):
        self.robot_attack_power = weapon.weapon_power

    def robot_attack(self, dinosaur):
        dinosaur.dinosaur_health -= self.robot_attack_power


