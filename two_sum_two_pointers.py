'''
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use  O(1) additional space.'''


from typing import List
def twoSum(numbers: List[int], target: int) -> List[int]:
        dict1={}
        for i in range(0, len(numbers)):
                compliment =  target -numbers[i]
                if compliment not in dict1.keys():
                        dict1[numbers[i]]=i+1
                else:
                        return [dict1[compliment],i+1]
        return []

print(twoSum([2,3,4],6))