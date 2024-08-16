# Import the array module
import array

# Creating an array of signed integers ('i' typecode stands for signed integers)
my_array = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])

# Function to delete an element from the array
def deleteElement(inputArray, element):
    try:
        # Attempt to remove the element from the array
        inputArray.remove(element)
    except ValueError:
        # If the element is not found, print an error message
        print(f"Element {element} not found in the array.")
    return inputArray

# Deleting the element 6 from the array and printing the updated array
print("Array after deleting 6:", deleteElement(my_array, 6))

# Attempting to delete an element that is not in the array
# This should print an error message and return the unchanged array
print("Array after attempting to delete 10:", deleteElement(my_array, 10))
