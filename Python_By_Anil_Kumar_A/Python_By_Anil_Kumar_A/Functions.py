'''
--------------------------------------------------
Title:         Funtions_Python.py
Description:   Useful to understand functions in
               Python
Owner:         Anil Kumar A
---------------------------------------------------
'''

'''
-----------------------------
Subroutine Name: puts
Usage:           puts('I|W|E', message to print)
'''

def puts(msg, lvl = 'I'):
    if lvl == 'I':
        print('INFO: ', msg)
    elif lvl == 'W':
        print('WARN: ', msg)
    else :
        print('ERROR: ', msg)
    return;


def changeList(list_name):
    list_name.append(['a', 1.2, (1, 2), {'a':1, 'b':2}])
    return;


def configInterfaceIp(IfName, Unit, IpAddr):
    cmd = 'set '+IfName+' unit.'+Unit+' family inet address '+IpAddr
    print('\t', cmd)
    return

def testVarArgs(var1, *var2):
    print('var1 is: ', var1)
    for var in var2:
        print('var2 element: ', var)
    return

def testReturn(IfName, Unit, IpAddr):
    cmd = 'set '+IfName+' unit.'+Unit+' family inet address '+IpAddr
    return cmd

def testVarScope(var1):
    testVar = var1
    print('Local value for testVar is: ', testVar)
    #return




print('===========>Functions=01')
puts('He is working alot', 'I')
puts('He is not working', 'E')


print('===========>Functions=02, by referance')
my_list = [1, 2, 3, 4]
print('My List before Calling function is: ', my_list)
changeList(my_list)
print('My List after Calling function is: ', my_list)

print('======>Keyword Arguments')
configInterfaceIp(IfName = 'ge-0/0/0',\
                  Unit   = '0',\
                  IpAddr = '10.204.39.102/24')


print('=======>Variable Length Arguments')
print('Passing only 2 Args')
testVarArgs(1, 2)
print('Passing multiple Args')
testVarArgs(1, 2, 3, 4, 5, 6)

print('=======>Retun')
cmd = testReturn(IfName = 'ge-0/0/0',\
                 Unit   = '0',\
                 IpAddr = '10.204.39.102/24')
print('Returned Value is: ', cmd)
                  

print('========Local Vs Global Vars')
testVar = 0
testVarScope(100)
print('Global value for testVar is: ', testVar)


                  



