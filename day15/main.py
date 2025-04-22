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
