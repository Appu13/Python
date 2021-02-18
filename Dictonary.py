'''
Dictonaries :

Mutatble
Unordered 
Key - Value pair
No duplicate keys

General format dictonary name = {key:value}

@author: Appu13
'''

#Months in a year
months = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'Ma': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep': 'September',
    'Oct': 'October',
    'Nov': 'Noveber',
    'Dec': 'December',
    }

# Printing the dictionary
print(months)

# Printing the keys int the dictionary
print("Dictonary Keys: ",months.keys())

# Printing the values in the dictionary
print("Dictonary Values ",months.values())

# Updating value in dictonary
months.update({'Nov':'November',})
print(months)

# Printing the items in the ditconary
print(months.items())

# Iterating over the dictionary
for key,value in months.items():
    print(key)
    print(value)
