# Program to display the fibonacci
# sequence up to n-th tern where
# n is provided by the user

# take input from the user
nterms = int(input("How many terms? "))

# first two terms
n1 = 0
n2 = 1
count = 2

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence:")
   print(n1)
else:
   print("Fibonacci sequence:")
   #print(n1,",",n2)
   while count < nterms:
       nth = n1 + n2
       print(nth)
       # update values
       n1 = n2
       n2 = nth
       count += 1
