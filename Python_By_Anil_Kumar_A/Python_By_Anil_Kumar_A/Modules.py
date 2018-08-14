
print('======> Scoping Example')
global Money
Money = 2000
def AddMoney():
   # Uncomment the following line to fix the code:
    #global Money
    Money = Money + 1

print(Money)
AddMoney()
print(Money)

print('==========> dir example')

# Import built-in module math
import math

content = dir(math)

print(content)
