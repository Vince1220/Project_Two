from Robot import Robot
class Dinosaur:
    def __init__(self,name,attack_power,health):
        self.name=''
        self.attack_power-=25
        self.health = 100
    

    def attack_robot(self, robot):
        robot.power -= self.attack_power
        print (f'{Dinosaur.name} attacks {Robot.name} with a bite')
        print (f'{Robot.name} has {robot.power} remaining')


    def set_name(self):
        self.name = input("Please enter name")    


#check point

        pass