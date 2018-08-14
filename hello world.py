print('hello,world!')
#this program add two number
#number are provided by the user
#input
a=input('inter the value of a: ')
b=input('inter the value of b: ')
#adding
sum=float(a)+float(b)
#display
print('The sum of {0} and {1} is {2}'.format(a,b,sum))
#python program to calculate the square root
num=float(input('enter a number: '))
num_sqrt=num**0.5
print('The square root of %0.3f is %0.3f'%(num,num_sqrt))
#python program to find the area of triangle
a=float(input('enter the value of a: '))
b=float(input('enter the value of b: '))
c=float(input('enter the value of c: '))
#calculate perimeter
s=(a+b+c)/2
#calculator area
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('The area of triangle is %0.3f'%area)

