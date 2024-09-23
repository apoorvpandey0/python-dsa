
Time: Best and Average n log n

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Choose the pivot
        left = [x for x in arr if x < pivot]  # Elements less than the pivot
        middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
        right = [x for x in arr if x > pivot]  # Elements greater than the pivot
        return quicksort(left) + middle + quicksort(right)  # Combine the sorted parts

# Example usage:
array = [10, 7, 8, 9, 1, 5]
sorted_array = quicksort(array)
print("Sorted array:", sorted_array)
