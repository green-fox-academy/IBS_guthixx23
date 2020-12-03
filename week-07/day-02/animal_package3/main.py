from animal_package3.farm import Farm
from animal_package3.animal import Animal

cat = Animal()
dog = Animal(30, 30)


cat.print_stats()


for i in range(10):
    cat.eat()
    cat.drink()

cat.print_stats()


dog.print_stats()

for i in range(20):
    dog.play()

dog.print_stats()


farm = Farm(3)

farm.add(dog)
farm.add(cat)

farm.breed()
farm.breed()
farm.slaughter()

farm.breed()