'''
Created on 10-Feb-2021

Program to swap the value of two integers without using temp variable

@author: Appu13
'''

a = int(input("Enter the first number "))
b = int(input("Enter the second number "))
print("Values before swapping ")
print("a = ", a, "b = ",b)

# Swapping 
a = a + b
b = a-b
b = a-b

print("Values after swapping")
print("a = ", a, "b = ",b)