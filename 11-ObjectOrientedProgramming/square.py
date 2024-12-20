class Square:
   def __init__(self, a):
      self.a = a
   def area(self):
      return self.a * self.a
   def peri(self):
      return 4 * self.a
   
      

square1 = Square(4)
square2 = Square(6)

print('Square with side 4:')
print(f'Area is {square1.area()}, Perimeter is {square1.peri()}')
print ('Square with side 6:')
print(f"Area is {square2.area()}, perimeter is {square2.peri()}")
