'''
Created on 12-Feb-2021

Program to demonstrate the different functions of a list in python

@author: Appu13
'''
from pip._vendor.chardet import langbulgarianmodel


# Creating a sample list
languages = ['C++', 'Java', 'Python', 1786,'C#', 'C']

# Printing the list as whole
print("Elements in the list: ",languages)

# Printing an item from a list with index
print("Element with the index 3: ", languages[3])

# Printing items in a range from a list
print("Printing elements in the range 0-3: ", languages[0:3])

# Printing items in reverse order
print("Printing the 2nd last element in the list: ", languages[-2])

# Printing the length of the list
print("Length of the list: ", len(languages))

languages2 = ['Kotlin', 'Ruby']

# Extending the list language
languages.extend(languages2)
print("List after extending: ", languages)

# Inserting langugaes into languages 2
languages2.insert(0, languages)
print("Languages 2 after insertion: ", languages2)

# Append function
languages.append("PHP")

# Remove function
languages.remove("C")
print("list after removing: ", languages)

# Pop function
print("Popped Element: ", languages2.pop())

# Reverse function
languages.reverse()
print("List after reversing: ", languages)

# Printing the index of a particular element form the list
print("Index of C#:", languages.index("C#"))

# Printing the occurrences of an element
languages.append("C#")
print("Number of occurrence of C#: ",languages.count("C#"))

# Sorting the list
languages.sort()
print("After Sorting: ",languages)

# Join functions
joined_list = '+'.join(languages)
print(joined_list)


# Clear function
languages.clear()
print("List after clearing ", languages)
