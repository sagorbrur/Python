#python program to find the largest
print('python program to find the largest: ')
a=float(input("enter first number: "))
b=float(input("enter second number: "))
c=float(input("enter third number: "))

if (a>b) and (a>c):
    largest=a
elif (b>a) and (b>c):
    largest=b
else:
    largest=c
print("The largest number is : ",largest)

#Checking prime in python
print("Checking prime in python::::")
num=int(input("enter a number: "))
#prime number are greater than 1
if num>1:
    #check for factor
    for i in range(2,num):
        if (num%i)==0:
            print(num,"is not a prime number")
            print(i,"times",num//i,"is",num)
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"si not a prime number")
