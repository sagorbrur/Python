while True:
    inputLine=input(">>>")
    if(inputLine in ["HI","Hi","hi","hI","HELLO","Hello","hello"]):
        print("Hello")
    elif(inputLine in ["What is Your Name?","What's your name?",
                       "Can I know your name?","your name?",
                       "Tell me your name","what's your name"]):
            print("My name is Sagor")
    else:
       print("Don't Understand") 
