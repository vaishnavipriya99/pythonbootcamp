class Animal:
    def speak():
        return "Animal is speaking"
class Dog(Animal):
    def bark():
        return "Bow.."
obj1=Animal
obj2=Dog
print(obj2.speak())
print(obj2.bark())
