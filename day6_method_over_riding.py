class Animal:
    def speak():
        return "Animal is speaking...."
class Dog(Animal):
    def speak():
        return "Dog is speaking...."
class Puppy(Dog):
    def speak():
        return "Puppy is speaking...."
obj2=Dog
print(obj2.speak())