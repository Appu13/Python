'''
Created on 14-Feb-2021

Sets:
Unique
Unordered 
Unindexed

@author: Appu13
'''

Unique_Numbers = {7,2,1,3,1,29,34,79,21,56,37,48,99,13,4,6,19}

Odd_Numbers = {1,3,5,7,9,11,13,15}

Even_Numbers = {0,2,4,6,8,10,12,14}

Prime_Numbers = {2,3,5,7,11,13,17,19}

print(Unique_Numbers)

Unique_Numbers.add(12)

print(Unique_Numbers)

# remove is used to remove an element from the set
Unique_Numbers.remove(2)

# Discard is used when you want to remove an element from the set but do not know if it exsits or not
Unique_Numbers.discard(4)

print(Unique_Numbers)

# Intersection is used to find the common elements between two sets
odd = Odd_Numbers.intersection(Unique_Numbers)
print("Odd Numbers: ",odd)

Even_Prime = Unique_Numbers.intersection(Even_Numbers,Prime_Numbers)
print("Even primes: ",Even_Prime)

# Difference is used to get the elements in the first set which are not present in the second set
diff = Odd_Numbers.difference(Unique_Numbers)
print("Difference: ",diff)

# Symmetric difference is used to find the elements , from both sets, which are not present in the other
print("Symmetric Difference: ",odd.symmetric_difference(Unique_Numbers))
