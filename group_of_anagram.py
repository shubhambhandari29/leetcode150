"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]"""
from collections import defaultdict

def anagram_check(v1,v2):
    v1_sort = ''.join(sorted(v1))
    v2_sort = ''.join(sorted(v2))  # if we simply do sorted(v1) ,  then output will be a list with each chars
    if(v1_sort == v2_sort):
        return True
    
def groupAnagrams(strs):
    list_f = []
    grouped = set()  # Set to track already grouped strings
    for i in range(len(strs)):
        if i not in grouped:
            list1 = [strs[i]]
            for j in range(i+1, len(strs)):
                if j not in grouped and anagram_check(strs[i], strs[j]):
                    list1.append(strs[j])
                    grouped.add(j)  # Marking j as grouped
            list_f.append(list1)
    return list_f

def correct_sol(strs):
    # Create a empty dictionary to store the grouped anagrams
    anagrams_dict = defaultdict(list)

    # Group the anagrams based on their sorted forms
    for word in strs:
        sorted_word = ''.join(sorted(word))
        print("SORTED WORDS", sorted_word)
        anagrams_dict[sorted_word].append(word)

    # Convert the dictionary values to a list of lists
    grouped_anagrams = list(anagrams_dict.values())

    return grouped_anagrams


print(correct_sol(["eat","tea","tan","ate","nat","bat"]))