class Animal:
    def speak():
        return "Animal is speaking"
class Dog(Animal):
    def bark():
        return "Bow.."
class Puppy(Dog):
    def puppy_speaking():
        return "i am puppy"
obj1=Animal
obj2=Dog
obj3=Puppy
print(obj3.speak())
print(obj3.bark())
print(obj3.puppy_speaking())
