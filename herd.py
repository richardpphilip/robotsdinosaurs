from dinosaur import Dinosaur

dinosaur_one = Dinosaur()
dinosaur_two = Dinosaur()
dinosaur_three = Dinosaur()

dinosaur_herd = [dinosaur_one, dinosaur_two, dinosaur_three]


class Herd:

    def dinosaur_herd_health(self):
        herd_health = dinosaur_one.dinosaur_health
        herd_health += dinosaur_two.dinosaur_health
        herd_health += dinosaur_three.dinosaur_health
        if herd_health == 0:
            print("all dinosaurs are dead, robots win!")
        elif herd_health != 0:
            print(herd_health)