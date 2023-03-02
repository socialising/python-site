#class to do...
class Circle:
  def __init__(self,radius):
     self.radius=radius

  def area(self):
    return 3.142*self.radius**2

  def perimeter(self):
      return 3.142*2*self.radius
c=Circle(6)   
print(c.area())
print(c.perimeter())


