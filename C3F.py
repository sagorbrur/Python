def C2F():
    Celsius = input('Enter degrees in Celsius:');
    Fahrenheit = (9.0/5.0)*Celsius+32;
    print Celsius,'Celsius=',Fahrenheit,'Fahrenheit';
    
def F2C():
    Fahrenheit = input('Enter degrees in Fahrenheit:');
    Celsius = ((Fahrenheit-32.0)/9.0)*5.0;
    print Fahrenheit,'Fahrenheit=',Celsius,'Celsius';
