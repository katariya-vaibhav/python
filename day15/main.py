# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to the target.

# Input: nums = [2, 7, 11, 15], target = 9  
# Output: [0, 1]  
# Explanation: nums[0] + nums[1] == 2 + 7 == 9


def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

# Example
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]


# ------------------------------------------------

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element is greater than the next
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

arr = [5, 2, 9, 1, 5, 6]
print("Original array:", arr)
sorted_arr = bubble_sort(arr.copy())
print("Sorted array:", sorted_arr)

