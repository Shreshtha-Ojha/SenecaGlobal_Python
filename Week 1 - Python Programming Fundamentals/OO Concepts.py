#class, object
class car:
  def __init__(self,model,year):
    self.model = model
    self.year = year

  def show(self):
    print(f"The name of the model is {self.model} ,and was launched in the year {self.year}")

c1 = car("Corolla" , 2020 )
c2 = car("Camry" , 2024) 
c1.show()                #output: The name of the model is Corolla ,and was launched in the year 2020
c2.show()                #output: The name of the model is Camry ,and was launched in the year 2024

#Inheritance

class parent:
    def noise(self):
        print("Animal speaks to communicate")

class Dog(parent):
    def bark(self):
        print("Dog barks")
d = Dog()
d.noise() 
d.bark()  

#output
#Animal speaks to communicate
#Dog barks
#Using the Super() function
class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"Name: {self.name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  
        self.breed = breed

    def info(self):
        super().info()
        print(f"Breed: {self.breed}")

d = Dog("Leo", "Golden Retriever")
d.info()


#Method Overriding
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()                      # Output: Dog barks




