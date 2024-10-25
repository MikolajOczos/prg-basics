###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides

import math


def triangle_area(a,b,c): 
    s = (a+b+c)/2
    result = math.sqrt((s)*(s-a)*(s-b)*(s-c))
    return result
a = float(input("a?"))
b=float(input("b?"))
c=float(input('c?'))

final_area = triangle_area(a,b,c)

print(f'The area of ​​a triangle with sides {a},{b},{c} is {final_area}')
