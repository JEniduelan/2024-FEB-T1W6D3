# Non-primitive data types - hold/stores multiple pieces of data

# List - Array - collection of data - indexed - multable (changed)
numbers = [ 13, 2, 5, 98, 56 ]
#            0  1  2   3   4

print(numbers)
print(numbers[2])

numbers[2] = 10
print(numbers)
#append means add at the end of the list
numbers.append(42)
print(numbers)
#insert means add and position data from the list
numbers.insert(0, 16)
print(numbers)
#pop means remove data from the end of the list
numbers.pop()
print(numbers)
#remove means remove data from the list
numbers.remove(98)
print(numbers)
#sort means sort ascending
numbers.sort()
print(numbers)
#reverse means sort desascending
numbers.reverse()
print(numbers)
#it will show length of the string
print(len(numbers))

# index, count
print ("\n\n\n\n")

# Tuple - collection of data - indexed - immutable (cannt be changed)

names = ( "John", "Jane" , "Mike" )
#            0      1         2

print(names)
print(names[1])
names[2] = "Steve"

days_of_the_week = ("Monday", "Tuesday", "Wednesday", "...")
co_ordinates_of_some_famous_place = (123.56, 20.2)

