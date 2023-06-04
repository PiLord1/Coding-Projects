from Animal import Animal
class Fish(Animal):
    def __init__(self, name):
        self._name = name
    def sound(self):
        return "{} says blub blub.".format(self._name)
    def move(self):
        return "{} swims.".format(self._name)
    def habitat(self):
        return "{} is aquatic environments.".format(self._name)
    def body(self):
        return "{} has fins.".format(self._name)
    
class Bird(Animal):
    def __init__(self, name):
        self._name = name
    def sound(self):
        return "{} says tweet tweet.".format(self._name)
    def move(self):
        return "{} flies.".format(self._name)
    def habitat(self):
        return "{} lives in aerial environments.".format(self._name)
    def skeletal(self):
        return "{}'s skeletal structure consists of hollow bones.".format(self._name)
    
class LandAnimal(Animal):
    def __init__(self, name):
        self._name = name
    def sound(self):
        return "{} says uga uga.".format(self._name)
    def move(self):
        return "{} moves.".format(self._name)
    def habitat(self):
        return "{} lives in terrestrial environments.".format(self._name)
    def temperature(self):
        return "{}'s surroundings have varying temperatures.".format(self._name)

class Two_legged(LandAnimal):
    def __init__(self, name):
        self._name = name
    def sound(self):
        return "{} says mhmmpf mhmmpf.".format(self._name)
    def move(self):
        return "{} hops.".format(self._name)
    def habitat(self):
        return "{} lives in woodlands.".format(self._name)
    def temperature(self):
        return "{}'s surroundings have hot summers and cold winters.".format(self._name)
    def strength(self):
        return "{}'s legs are capable for great endurance.".format(self._name)

class Four_legged(LandAnimal):
    def __init__(self, name):
        self._name = name
    def sound(self):
        return "{} says moo moo.".format(self._name)
    def move(self):
        return "{} walks.".format(self._name)
    def habitat(self):
        return "{} lives in woodlands.".format(self._name)
    def temperature(self):
        return "{}'s surrondings have warm climate.".format(self._name)
    def speed(self):
        return "{} can sprint faster.".format(self._name)

class No_legs(LandAnimal):
    def __init__(self, name):
        self._name = name
    def sound(self):
        return "{} says hiss hiss.".format(self._name)
    def move(self):
        return "{} slithers.".format(self._name)
    def habitat(self):
        return "{} lives in forests.".format(self._name)
    def temperature(self):
        return "{}'s surrondings have temperate climate.".format(self._name)
    def eat(self):
        return "{} can swallow large prey.".format(self._name)
    
fish = Fish("Bitch")
print("Fish:")
print(fish.sound())
print(fish.move())
print(fish.habitat())
print(fish.body())
print("\nBird:")
bird = Bird("Tweetie")
print(bird.sound())
print(bird.move())
print(bird.habitat())
print(bird.skeletal())
land = LandAnimal("Caesar")
print("\nLand Animal:")
print(land.sound())
print(land.move())
print(land.habitat())
print(land.temperature())
print("\nBunny:")
bunny = Two_legged("Bugs")
print(bunny.sound())
print(bunny.move())
print(bunny.habitat())
print(bunny.temperature())
print(bunny.strength())
print("\nBitch:")
ano_to = Four_legged("Jephen")
print(ano_to.sound())
print(ano_to.move())
print(ano_to.habitat())
print(ano_to.temperature())
print(ano_to.speed())
print("\nSnake:")
snake  = No_legs("Orochimaru")
print(snake.sound())
print(snake.move())
print(snake.habitat())
print(snake.temperature())
print(snake.eat())
print("\nProgram finished.")