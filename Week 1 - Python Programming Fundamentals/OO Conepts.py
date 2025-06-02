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


