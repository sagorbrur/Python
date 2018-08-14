#python program for swap two number
x=input('enter value of x: ')
y=input('enter value of y: ')
#creat a temporary template and swap
temp=x
x=y
y=temp
print('The value of x after swapping: {}'.format(x))
print('The value of x after swapping: {}'.format(y))

#another way
print('another method...')
x=input('enter value of x: ')
y=input('enter value of y: ')
x=x+y
y=x-y
x=x-y

print('The value of x after swapping: {}'.format(x))
print('The value of x after swapping: {}'.format(y))


#another method
print('another method...')
x=input('enter value of x: ')
y=input('enter value of y: ')

x=x*y
y=x/y
x=x/y
print('The value of x after swapping: {}'.format(x))
print('The value of x after swapping: {}'.format(y))

print('another method...')
x=input('enter value of x: ')
y=input('enter value of y: ')
x=x^y
y=x^y
x=x^y
print('The value of x after swapping: {}'.format(x))
print('The value of x after swapping: {}'.format(y))
