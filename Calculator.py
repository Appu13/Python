'''
A calculator 
@author: Appu13
'''



a = float(input("Enter the first number "))
b = float(input("Enter the second number "))
ops = input("Enter the operation ")
if ops == '+':
    print("Sum = ", (a+b))
        
elif ops == '-' :
    print("Difference = ", (a-b))
    
elif ops == '*':
    print("product = ", (a*b))

elif ops == '/':
    print("Quotient = ", round((a/b),2))

else:
    print("Wrong operation")  
 
