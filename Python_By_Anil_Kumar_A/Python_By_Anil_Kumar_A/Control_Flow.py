a = 90
b = 20

c = 'Anil'
d = 'Kumar'

print('==============>IF-ELSE')

if c == d :
    print('"c" is equals to "d"', c,"==",d)
else :
    print('"c" is not equals to "d"', c,"!=",d)

print('===============>IF-ELSEIF-ELSE')
if a <= 10:
    print("<<<<<=====")
elif 11 <= a <=20 :
    print("20")
else:
    print(">20")

print('===========>While')
count = 0
while count < 5:
   print (count, " is  less than 5")
   count = count + 1
else:
   print (count, " is not less than 5")

print('============>For')
a = {1:'one', 2:'two', 3:'three', 4:'four'}

for key_value in a.keys():
    print(key_value, "==", a[key_value])

