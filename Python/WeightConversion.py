'''
A Python program to convert weight form kilogram to pounds

@author: Appu13
'''
# Get the input from the use as a float
weight_kilograms = float(input("Enter your weight in Kilograms(kg)"))

# Conversion
weight_pounds = weight_kilograms * 2.20462262185

print(round(weight_pounds,2), " is your weight in pounds")