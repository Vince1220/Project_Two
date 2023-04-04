from Dinosaur import Dinosaur
from Robot import Robot



class Battlefield:
    def __init__(self):
      self.robot= Robot()
      self.dinosaur= Dinosaur()

     
     
     
    def run_game(self):
       self.display_welcome()
       self.battle_phase()

    def display_welcome(self):
        print ('Welcome to Lizards X Mechs!! Only one can win. Decide the Destiny!')
        self.robot.set_name()
        self.dinosaur.set_name()

    def battle_phase(self):
       self.robot.Attack(self.dinosaur)
       self.dinosaur.attack_robot(self.robot)
       if Dinosaur.health<= 0:
        print (f'{Dinosaur.name} has died!') 
       
       elif Robot.power<=0:
          print (f'{Robot.name} has been Terminated!')
          
    def display_winner(self):
       if Dinosaur.health <=0:
          print (f'{Dinosaur.name} Wins!!!')
       elif Robot.power <= 0:
          print (f'{Robot.name} Wins!!!')
            



        