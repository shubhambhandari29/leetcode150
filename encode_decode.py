'''
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode
'''

from typing import List
def encode(strs: List[str]) -> str:
        if strs == []:
               return 'null'
        s:str =''
        for i in strs:
                i = i[::-1]
                s = s + '>' + i
        print("s",s)
        return s
            

def decode(s: str) -> List[str]:
        if s == 'null':
               return []
        l = s[1:]
        l = l.split('>')
        l1=[]

        for i in l:
            l1.append(i[::-1])
        return l1

print(encode(["we","say",":","yes"]))
print(decode(':teen:edoc:evol:uoy'))