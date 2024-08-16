# Import the array module
import array

# Creating an array of signed integers ('i' typecode stands for signed integers)
my_array = array.array('i', [2, 4, 6, 8, 10])

# Printing the initial array
print("Initial array:", my_array)

# Inserting an element into the array
# Syntax: array.insert(index, value)
# Inserts the value 12 at index 5 (end of the array in this case)
my_array.insert(5, 12)

# Printing the array after insertion
print("Array after insertion:", my_array)

# Inserting an element at the beginning of the array
# Inserts the value 1 at index 0
my_array.insert(0, 1)
print("Array after inserting 1 at index 0:", my_array)

# Inserting an element in the middle of the array
# Inserts the value 5 at index 3
my_array.insert(3, 5)
print("Array after inserting 5 at index 3:", my_array)

# Trying to insert an element at an index greater than the array length
# Inserts the value 20 at index 10, which is beyond the current array length
# The element will be appended at the end of the array
my_array.insert(10, 20)
print("Array after inserting 20 at index 10:", my_array)
