from pet import Pet


class Person:
    def __init__(self, firstName, lastName, treats, petFood, pet):
        self.firstName = firstName
        self.lastName = lastName
        self.treats = treats
        self.petFood = petFood
        self.pet = pet

    def walk(self, pet):
        Pet.play(pet)
        return self

    def feed(self):
        Pet.eat()
        return self

    def bathe(self):
        Pet.noise()
        return self


lily = Pet("lily", "cat", "meowing loudly")
yoni = Person("yoni", "kohen", 0, 0, lily)

yoni.walk(lily)
lily.display()
