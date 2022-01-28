""" 
    Given an integer array arr, return the length of the longest subarray, which is a mountain.
    Return 0 if there is no mountain subarray.
    https://leetcode.com/problems/longest-mountain-in-array/
"""


class Solution:

    # Algorithm
    # Find a peak
    # find previous valley or start of the array for that peak
    # find next valley or end of the array for that peak
    # mountain length = next - last + 1

    # Runtime 172 ms
    def longestMountain(self, arr):
        answer = 0
        for i in range(1, len(arr) - 1):
            # Finding peak
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                # print("Peak at", i)

                # (arr[j]<arr[j-1] and arr[j]<arr[j+1]) or (arr[j]<=arr[j-1] and arr[j]<arr[j+1]) or (arr[j]<arr[j-1] and arr[j]<=arr[j+1])
                # This covers the valleys case of  101 , 001, 100

                # :TODO: Check if this is correct
                # or just simply (arr[j]<=arr[j-1] and arr[j]<=arr[j+1]) ?

                # Finding left valley
                left = 0
                j = i - 1
                while j > 0:
                    if (arr[j] < arr[j - 1] and arr[j] < arr[j + 1]) or (
                            arr[j] <= arr[j - 1] and arr[j] < arr[j + 1]) or (
                                arr[j] < arr[j - 1] and arr[j] <= arr[j + 1]):
                        # print("Left valley at",j)
                        left = j
                        break
                    j -= 1

                # Finding right valley
                right = len(arr) - 1
                j = i + 1
                while j < len(arr) - 1:
                    if (arr[j] < arr[j - 1] and arr[j] < arr[j + 1]) or (
                            arr[j] <= arr[j - 1] and arr[j] < arr[j + 1]) or (
                                arr[j] < arr[j - 1] and arr[j] <= arr[j + 1]):
                        # print("Rjght valley at",j)
                        right = j
                        break
                    j += 1
                # print(left,right)

                # Set the longest mountain length
                if right - left + 1 > answer:
                    answer = right - left + 1
        return (answer)


# print(Solution().longestMountain([0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]))  # 11
# print(Solution().longestMountain([2, 1, 4, 7, 3, 2, 5]))  # 5
print(Solution().longestMountain([2, 2, 2]))  # 0
# print(Solution().longestMountain([1, 1, 0, 0, 1, 0, 0]))  # 3
