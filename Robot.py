from Dinosaur import Dinosaur
from Weapon import Weapon
class Robot:
    def __init__ (self,name,power,active_weapon):
        self.name= ''
        self.power=100
        self.active_weapon=Weapon()

    def Attack(self,dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print (f'{Robot.name} attacks {dinosaur.name} with {Weapon.name}')
        print (f'{dinosaur.name} has {dinosaur.health} remaining')
    
    def set_name(self):
        self.name = input("Please enter name")
        print('name')

    def set_weapon (self):
        self.active_weapon = Weapon.name
        print(Weapon.name)
        



