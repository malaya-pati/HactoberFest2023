def bubble_sort(arr):
    """
    Perform bubble sort on the given array.

    Parameters:
    arr (list): An array of elements.

    Returns:
    list: The sorted array.
    """
    n = len(arr)

    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already in place, so no need to check them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

# Example usage
unsorted_array = [64, 34, 25, 12, 22, 11, 90]

print("Unsorted array:", unsorted_array)
sorted_array = bubble_sort(unsorted_array)
print("Sorted array:", sorted_array)
