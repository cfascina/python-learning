from collections import namedtuple

dog = namedtuple('dog', 'name age breed')

rex = dog(name = 'Rex', age = 2, breed = 'Golden Retriever')
liz = dog(name = 'Liz', age = 3, breed = 'German Shepherd')
sam = dog(name = 'Sam', age = 5, breed = 'Bulldog')

print("List of dogs:")
print("-------------")

print("\nName: " + rex.name)
print("Age: " + str(rex.age))
print("Breed: " + rex.breed)

print("\nName: " + liz.name)
print("Age: " + str(liz.age))
print("Breed: " + liz.breed)

print("\nName: " + sam.name)
print("Age: " + str(sam.age))
print("Breed: " + sam.breed)
