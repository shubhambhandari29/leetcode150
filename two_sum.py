"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [12,17,11,7,2], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]"""


def two_sum(nums, target):
     # Create a dictionary to store the indices of elements
    num_indices = {}

    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num

        # Check if the complement exists in the dictionary
        if complement in num_indices:
            # Return the indices of the current number and its complement
            print(num_indices)
            return [num_indices[complement], i]
        
        # If the complement doesn't exist, store the index of the current number
        num_indices[num] = i

    # If no solution is found, return an empty list
    return []

print(two_sum([1,3,5,7,8],15))