## animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):

    def play(self):
        print('This is the default play() method')

    pass


## dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ## dog has-a name
        self.name = name

    def play(self):
        print('woof. I overrode the play() method')


## cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        ## cat has-a name
        self.name = name


## person is-a object
class Person(object):

    def __init__(self, name):
        self.name = name

        ## person has-a pet of some kind
        self.pet = None


## employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## init from superclass/parent (Person)
        super(Employee, self).__init__(name)

        ## employee has-a salary
        self.salary = salary


## fish is-a object
class Fish(object):
    pass


## salmon is-a fish
class Salmon(Fish):
    pass


## halibut is-a fish
class Halibut(Fish):
    pass


## rover is-a dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary has-a pet (Cat)
mary.pet = satan

## frank is-a employee with 120k salary
frank = Employee("Frank", 120000)

## frank has-a pet (Dog)
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is-a halibut
harry = Halibut()

# study drills - inherited functions
frank.pet.play()
mary.pet.play()
