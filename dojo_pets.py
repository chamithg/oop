import re
from unicodedata import name


class Ninja:
    def __init__(self,first_name, last_name, pet_name, pet_type, pet_food, trick):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = Pet(name = pet_name,type= pet_type, noise= trick)
        self.pet_food = pet_food
    
    def walk(self):
        self.pet.play()
        return self
    
    def feed(self):
        self.pet.eat()
        if self.pet_food > 25:
            self.pet_food -= 25
        else:
            print("Not enough food.")
        return self
    
    def bathe(self):
        self.pet.noise()
        return self
    
    def __str__(self):
        return f"{self.first_name}'s {self.pet.type} named {self.pet.name}, health --> {self.pet.health} energy --> {self.pet.energy}"
        
    

# implement __init__( name , type , tricks ):
# implement the following methods:
# sleep() - increases the pets energy by 25
# eat() - increases the pet's energy by 5 & health by 10
# play() - increases the pet's health by 5
# noise() - prints out the pet's sound
    
class Pet:
    def __init__(self,name, type, noise) :
        self.name = name
        self.type = type
        self.health = 0
        self.energy = 0
        self.tricks = noise
        pass
    
    def sleep(self):
        self.energy +=25
        print(f"{self.name} is sleeping")

        
        return self
    
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} is eating")
        
        return self
    
    def play(self):
        self.health +=5
        print(f"{self.name} is playing")
        return self
    
    def noise(self):
        print(self.noise)
        return self
       
       
Ninja_chamith = Ninja("chamith", "gamage", "Kitty", "cat", 100, "meoww..." )  
   

print(Ninja_chamith)

Ninja_chamith.walk().feed().bathe()

print(Ninja_chamith)