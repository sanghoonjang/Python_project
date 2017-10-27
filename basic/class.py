# Make Class
class Prism:
  # Initialize attribute
  def __init__(self, width, height, depth):
    self.width = width
    self.height = height
    self.depth = depth
   
  # Method
  def content(self):
    return self.width*self.height*self.depth
 

# Make Object from Prism Class
p1 = Prism(10, 20, 30)
p1.content() # 6000
p1.height # 20

p1.height = 50 # Change Attribute 
p1.content() # 15000

p2 = Prism(50, 60, 70)
p2.content() # 210000
p2.height # 60


# Succession of Class
class Cube(Prism):
  def __init__(self, length):
    super().__init__(length, length, length)

c = Cube(20)
c.content() # 8000 


# Limit to add Attribute
class Klass:
  __slots__ = ["a", "b"]
  def __init__(self)
    self.a = 1

i = Klass()
i.a # 1

i.b = 2
i.b # 2

i.c = 3 # Error


# Property()
class Prop:
  def __ini__(self):
    self.__x = 0
  def getx(self):
    return self.__x
  def setx(self, x):
    self.__x = x

i = Prop()
i.x # Error
i.getx() # 0

class Prop:
  def __ini__(self):
    self.__x = 0
  def getx(self):
    return self.__x
  def setx(self, x):
    self.__x
  x = property(getx, setx)
  
i = Prop()
i.x # 0
