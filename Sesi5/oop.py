raka = ["Raka Ardhi", 28, "CurDev", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]

print("Daftar nama: ", raka[0], spock[0], mccoy[0])
print("Daftar umur: ", raka[1], spock[1], mccoy[1])
print("Daftar jabatan: ", raka[2], spock[2], mccoy[2])
print("Daftar tahun mulai: ", raka[3], spock[3], mccoy[2])

class Dog:
    pass

class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

dog_1 = Dog('Miley', 9)
#.__init__(dog_1, 'Miley', 9)

dog_2 = Dog('Hike', 2)
#.__init__(dog_2, 'Hike', 2)

dog_3 = Dog('Scrotby', 18)
#.__init__(dog_3, 'Scrotby', 18)

print("Dog 1 :: ", dog_1.name, dog_1.age)
print("Dog 2 :: ", dog_2.name, dog_2.age)
print("Dog 3 :: ", dog_3.name, dog_3.age)

print("\nSpecies")
print("Dog 1 ", dog_1.species)
print("Dog 2 ", dog_2.species)
print("Dog 3 ", dog_3.species)

# instance methods
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

dog_1 = Dog('Miley', 9)
buddy = Dog("Buddy", 9)

print(buddy.description())
print(dog_1.description())

print(dog_1.speak("Woof Woof"))
print(dog_1.speak("Bow Bow"))


# Inherit from other classes
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")

## Subclass of Dog (Inheritance)
# define that Bulldogs is a subclass of Dog
class Bulldogs(Dog):
    #sudah dipanggil dengan menggunkan inherit Dog
    # def __init__(self, name, age, breed):
    #     self.name = name
    #     self.age = age
    #     self.breed = breed

    # Instance method
    # def description(self):
    #     return f"{self.name} is {self.age} years old"

    #Another instance method
    def speak(self):
        return f"{self.name} says Woof Woof"

# define that Dachshund is a subclass of Dog
class Dachshund(Dog):
    #another instance method
    def speak(self):
        return f"{self.name} says Yap Yap"


#Extend the functionality of a parent class
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"

miles = JackRussellTerrier("Miles", 4, "Terrier")
miles.speak()
miles.speak("Grrr")