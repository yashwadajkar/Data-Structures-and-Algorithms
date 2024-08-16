# Import the array module
import array

# Creating an array of signed integers ('i' typecode stands for signed integers)
my_array = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])

# Function to traverse the array and print each element
def traverseArray(inputArray):
    # Loop through each element in the array
    for element in inputArray:
        # Print the current element
        print(element)

# Calling the function to traverse and print the elements of my_array
traverseArray(my_array)