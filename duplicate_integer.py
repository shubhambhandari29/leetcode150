#Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.


def hasDuplicate(nums) -> bool:
        hashset=set()
        for i in nums:
            if i in hashset:
                return True
            else:
                hashset.add(i)
        return False
    

print(hasDuplicate([1,2,5,6,7,8,8]))