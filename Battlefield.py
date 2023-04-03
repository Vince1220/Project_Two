

from Dinosaur import Dinosaur
from Robot import Robot



class Battlefield:
    def __init__(self):
      self.robot= Robot()
      self.dinosaur= Dinosaur()

     
     
     #def run_game(self):

    def display_welcome(self):
        print ('Welcome to Lizards X Mechs!! Only one can win. Decide the Destiny!')
        self.robot.set_name()

    def battle_phase(self):
       self.robot.Attack(self.dinosaur)
       self.dinosaur.attack_robot(self.robot)
          
        #def display_winner(self):



        