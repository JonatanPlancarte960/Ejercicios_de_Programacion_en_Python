# Single inheritance

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):

    # Class variable
    species = "Canis lupus familiaris"

    def __init__(self, name, breed):
        # This is a instance variable because it is declared in the constructor and can only be used at the instance level
        
        super().__init__(name)

        if not isinstance(name, str):
            raise ValueError("The Dog name must be a string")
        if not isinstance(breed, str):
            raise ValueError("The Dog breed must be a string")
        
        # self.__name = name - This is a public variable
        self.__breed = breed # This is a private variable

    # Getters & Setters

    # This is the getter the dog's breed - This can get the breed
    def get_breed(self):
        return self.__breed

    # This is the setter the dog's breed - This can set the dog's breed

    def set_breed(self, breed):
        self.__breed = breed
    
    def bark(self):
        print(f"{self.name} WOOF! WOOF! ARF!")

puppy = Dog("Puppy", "Labrador Retriever") # Instance method
lola = Dog("Lola", "Poodle")

print(puppy.name)
print(puppy.get_breed())
print(puppy.species)
puppy.bark()

print(lola.name)
print(lola.get_breed())
print(lola.species)
lola.bark()