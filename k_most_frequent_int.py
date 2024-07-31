'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.'''

from collections import Counter
def topKFrequent(nums : list, k: int):
        # Count the frequency of each element in the list
        frequency_count = Counter(nums)
    
        # Get the k most common elements based on frequency
        most_common_elements = frequency_count.most_common(k)
    
        # Extract the elements from the most common elements list
        top_k_elements = [element for element, _ in most_common_elements]
    
        return top_k_elements
      
      


               
    

print(topKFrequent([1,1,1,3,1,3,2,2,2,2,2,3,3,2,3],2))
        