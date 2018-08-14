#python program to convert temperature in
#Celsius to farenheit

print('celsius to fahrenheit')
celsius=float(input('Enter degree celsius: '))
fahrenheit=(celsius*1.8)+32
print('%0.1f degree celsius is equal to %0.1f degree fahrenheit.'%(celsius,fahrenheit))
#fahrenheit to celsius
print('fahrenheit to celsius')
fahrenheit=float(input('enter degree fahrenheit: '))
celsius = (fahrenheit - 32) / 1.8

print('%0.1f degree fahrenheit is equal to %0.1f degree celsius.'%(fahrenheit,celsius))
      
