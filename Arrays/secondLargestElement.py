def second_largest(arr):
    if len(arr) < 2:
        return None  # Not enough elements

    first = second = float('-inf')

    for number in arr:
        if number > first:
            second = first
            first = number
        elif first > number > second:
            second = number

    return second if second != float('-inf') else None

# Example usage:
arr = [3, 5, 1, 2, 4]
result = second_largest(arr)
