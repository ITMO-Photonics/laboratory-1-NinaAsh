import math 
def calculate(R, L):
    return math.pi*(R**2)*L
    
R = int(input('Please Enter the radius of a Cylinder: '))
L = int(input('Please Enter the length of a Cylinder: '))

print(calculate(R, L))
