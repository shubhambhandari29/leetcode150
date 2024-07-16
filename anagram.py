
'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false'''


def valid_anagram(v1,v2):
    s1,s2={},{}

    for i in v1:
        s1[i] =s1.get(i,0) +1

    for i in v2:
        s2[i] =s2.get(i,0) +1

    if s1 == s2:
        return True
    return False


def impl2(v1,v2):
    v1_sort = ''.join(sorted(v1))
    v2_sort = ''.join(sorted(v2))  # if we simply do sorted(v1) ,  then output will be a list with each chars
    print(v1_sort, v2_sort)
    if(v1_sort == v2_sort):
        return True


print(impl2('anagram','naamgra'))

#we can use Counter(v1) == Counter(v2) too. It is not advisable though