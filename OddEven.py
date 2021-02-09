'''
Program to test a set of numbers for odd even

@author: Appu13
'''

numbers = {7,8,9,10,11,12,13,14,15,16,17,18,19,20,55,66,34,33,87}
for number in numbers:
    if(number%2)==0:
        print(number,"is even")
    else:
        print(number,"is odd")