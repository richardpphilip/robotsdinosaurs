if __name__ == '__main__':
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


class Dinosaur:
    def __init__(self, dinosaur_type='mean'):
        self.dinosaur_type = dinosaur_type
        self.dinosaur_health = 100
        self.dinosaur_energy = 10
        self.dinosaur_attack_power = 5

    def dino_attack(self, robot, ):
        robot.robot_health -= self.dinosaur_attack_power
