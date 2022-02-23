"""
    Search an element in sorted array of unknown size
    Constraint: You cannot use the size of the array to find the index of the element.
    https://just4once.gitbooks.io/leetcode-notes/content/leetcode/binary-search/702-search-in-a-sorted-array-of-unknown-size.html
"""

# Algorithm
# Iterate the array in multiples of 2 (say)
# At some point you'll be at an index whose value is greater than the target element
# Make this element index your high in binary search
# And make the last checked element your low in binary search
# Now since we know the bounds and the target is in b/w them, apply boinary search to find the element
