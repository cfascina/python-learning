class Animal():
    def __init__(self, name):
        self.name = name
    def speak(self):
        raise NotImplementedError("Sublcasses must implement abstract method.")

class Dog(Animal):
    def speak(self):
        return self.name + " says woof!"

class Cat(Animal):
    def speak(self):
        return self.name + " says meow!"

class Bear(Animal):
    def __init__(self, name, hibernate = "yes"):
        Animal.__init__(self, name)
        self.hibernate = hibernate

rex = Dog('Rex')
felix = Cat('Felix')
pooh = Bear('Pooh')

print(f"From Dog(): {rex.speak()}")
print(f"From Cat(): {felix.speak()}")
print(f"From Bear(): {pooh.name}")
print(f"From Bear(): {pooh.hibernate}")
