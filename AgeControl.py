'''
A program to check if the applicant is eligible or not based on the base age

@author: Appu13
'''

minage = input("Enter the minimum age ")

agetocheck = input("Enter the age to check ")

if agetocheck >= minage:
    print("Person can come in")
else:
    print("Person cannot come in")