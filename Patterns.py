'''
Created on 10-Feb-2021

Program to print the following pattern based on user input
example: n = 5
 *****
 ****
 ***
 **
 *  

@author: Appu 13
'''

n = int(input("Enter the value of n "))
for a in range(n):
    for b in range((n-a)):
        print("*", end=' ')
    print()