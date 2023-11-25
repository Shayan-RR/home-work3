 # get array from user
def get_array():
  # Get size 
  size = int(input("Enter the size of the array: "))
  array = []

  # Get the elements
  for i in range(size):
    element = int(input(f"Enter element {i + 1}: "))
    array.append(element)

  return array
array = get_array()

# Print the array
print("your array is: ")
print(array)


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])

    return merge(left_array, right_array)

def merge(left_array, right_array):
    merged_array = []
    while left_array and right_array:
        if left_array[0] <= right_array[0]:
            merged_array.append(left_array.pop(0))
        else:
            merged_array.append(right_array.pop(0))

    merged_array += left_array or right_array

    return merged_array

sorted_array = merge_sort(array)

print()
print("your sorted array is: ")
print(sorted_array)
