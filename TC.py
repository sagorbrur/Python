#Temperature convertor
def displayMenu():
    print 'Temperature converter menu';
    print '(1) Convert Fahrenheit to Celsius';
    print '(2) Convert Celsius to Fahrenheit';
    print '(3) Convert Celsius to Kelvin';
    print '(4) Convert Kelvin to Celsius';
    print '(5) Convert Fahrenheit to Kelvin';
    print '(6) Convert Kelvin to Fahrenheit';
 def select():
        displayMenu();
        choice = input('Enter your choice number:')
        if(choice == 1):
            F2C();
         elif(choice == 2):
                C2F();
        elif(choice == 3):
                C2K();
         elif(choice == 4):
                 K2C();
         elif(choice == 5):
                F2K();
        elif(choice == 6):
            K2F();
        else:
         print"invalid choice:",choice;
                        
   
def C2F():
    Celsius = input('Enter degrees in Celsius:');
    Fahrenheit = (9.0/5.0)*Celsius+32;
    print Celsius,'Celsius=',Fahrenheit,'Fahrenheit';
    
def F2C():
    Fahrenheit = input('Enter degrees in Fahrenheit:');
    Celsius = ((Fahrenheit-32.0)/9.0)*5.0;
    print Fahrenheit,'Fahrenheit=',Celsius,'Celsius';
def C2K():
     Celsius = input('Enter degrees in Celsius:');
    Kelvin = Celsius+273;
    print Celsius,'Celsius=',Kelvin,'Kelvin';
def K2C():
     Kelvin = input('Enter degrees in Kelvn:');
    Celsius = Kelvin-273;
    print Kelvin,'Kelvin=',Celsius,'Celsius';
