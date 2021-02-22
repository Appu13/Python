'''

LEGB: local enclosing global and built in variables

'''

'''
Global and local variables
'''
# Global variable
num = 2

def printR():
    # Local variable: vaild only in the fuction
    num1 = 3
    print(num1)

printR()
print(num)


'''
Enclosing variable
'''
a = 'Global a'

def outer():
    
    # Enclosed variable
    b = 'Enclosing b'
    
    def inner():
        a = 'local a'

        print(a) # Gives the local variable
        print(b) # Gives the enclosed variable
    
    inner() 
    print(a) # Gives the Global variable

outer()

'''
Built in variables are those defined in python
if we use the same name the definiton we give will be used and not the one defined
hence we must be careful when using built in variable name
'''