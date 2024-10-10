# Recursive function to search for a number in the list
def recursive_search(arr, target, index=0):
    # Base case: if index exceeds the length of the list
    if index == len(arr):
        return -1  # Target not found in the list

    # If the current element matches the target, return the index
    if arr[index] == target:
        return index

    # Recursive case: move to the next element in the list
    return recursive_search(arr, target, index + 1)

# Input list and target number from the user
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
target = int(input("Enter the number to search for: "))

# Call the recursive search function
result = recursive_search(numbers, target)

# Output the result
if result != -1:
    print(f"Number {target} found at index {result}.")
else:
    print(f"Number {target} not found in the list.")
