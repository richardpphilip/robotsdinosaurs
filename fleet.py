from robot import Robot

robot_one = Robot()
robot_two = Robot()
robot_three = Robot()

robot_fleet = [robot_one, robot_two, robot_three]


class Fleet:

    def robot_fleet_health(self):
        fleet_health = robot_one.robot_health
        fleet_health += robot_two.robot_health
        fleet_health += robot_three.robot_health
        if fleet_health == 0:
            print("all robots are dead, dinosaurs win!")
        elif fleet_health != 0:
            print(fleet_health)
