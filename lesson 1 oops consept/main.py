class Toycar:
    color = 'red'
    wheels = 4

    def drive(self):
        print('vroom, the car is moving')
car_1 = Toycar()
car_1.drive()
car_2 = Toycar()
car_2.drive()

class Pets:
    def __init__(self,name,animal_type):
        self.name = name
        self.animal_type = animal_type

    def speak(self):
        if self.animal_type == 'dog':
            print(f'{self.name} says woof')
        elif self.animal_type == 'cat':
            print(f'{self.name} says meow')
        else:
            print(f'{self.name} makes a sound')


pet_1 = Pets('the rock','rock')
pet_1.speak()