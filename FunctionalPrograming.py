'''
Lambda functions do not have name
Anonymus or nameless functions
One time used
Reduce the size of code
Simple one line function that does not have def or any return keywords
'''

from functools import reduce

def addition(a,b):
    return a+b

lambda_addition = lambda x,y: x+y

print("Method result:", addition(2,3))
print("Lambda method", lambda_addition(2,3))

# Using lambda within functions
def RegNumber(x):
    return (lambda y: x+y)

# We first call the function by providing the parameter and store it into result
result = RegNumber(3811)
for i in range (100):
    # In result we supply the value needed for the lambda function
    print(result(i))


'''
Filter function are used to filter a list
They can take a lambda function and the list on which to be applied to

Map function are used to map a list or something to a function

Difference between map and filter:
 map will give the result of the operation
 filter will give the filtered result of the operation
'''

Number_List = [x for x in range(20)]
print("Filter Function: ", list(filter(lambda x: x % 2 == 0 , Number_List)))
print("Map Function: ", list(map(lambda x: x % 2 == 0 ,Number_List)))

'''
Reduce function is used reduce a given list 
'''

print("Reduce function: ", reduce(lambda y,x: x + y, Number_List))