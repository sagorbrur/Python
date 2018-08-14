#solve the quadratic equation by python
#ax**2+bx+c=0
#a,b,c are provided by the user

#import complex math module
import cmath
a=float(input('enter a: '))
b=float(input('enter b: '))
c=float(input('enter c: '))

#calculate discriminant
d=(b**2)-(4*a*c)
#find two solution
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(sol1,sol2))
