'''
Program to show iterations in the range function

@author: Appu 13
'''

# Getting the input from the user
StartPoint = int(input("Enter the start point of the list "))
EndPoint = int(input("Enter the end point of the list "))
IterationValue = int(input("Enter the iteration value "))

# Performing the iteration 
for element in range(StartPoint,EndPoint,IterationValue):
    print(element)
