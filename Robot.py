from Weapon import Weapon
class Robot:
    def __init__ (self,name,power,active_weapon):
        self.name= ''
        self.power=100
        self.active_weapon=Weapon()

    def Attack(self,dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
    
    def set_name(self):
        self.name = input("Please enter name")
        



