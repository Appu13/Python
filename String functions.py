'''
Program to show different python string functions

@author: Appu13

'''


string="Hey cows"

# Get the data type of the object
print(type(string))

# Concatenate the string
print(string, ", you are awesome")

# Convert to upper case
print("String in upper case form ",string.upper())

# Convert to lower case
print("String in lower case form ",string.lower())

# Get the length of the sting
print("Size of the string is ", len(string))

# Get the index of any character in string
print("The location of c ",string.index('c')+1)

# Extract character in a range
print("characters in the range 0-3 ",string[0:3])

# Multiple line string
longstring= """People are awesome
Top of the world""" 
print(longstring)


#replacing in string
new_message=longstring.replace("People","Cows")
print("Replaced message: ", new_message)

