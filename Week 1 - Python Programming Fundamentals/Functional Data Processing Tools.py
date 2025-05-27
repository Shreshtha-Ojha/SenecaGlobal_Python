# Lambda

def app(fx , value):
  return 6 +fx(value)

square = lambda x: x*x
avg = lambda x,y,z: (x+y+z)/3
print(square(5))              # 25
print(avg(3,5,10))            #6.0
print(app(lambda x: x*2, 2))  #10

# Mapping
def cube(l):
  return l*l*l

l = [1,4,2,6,7,8]
newl = []
newl = list((map(cube,l)))
print(newl)

