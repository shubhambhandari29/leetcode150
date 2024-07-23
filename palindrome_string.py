import re
def isPalindrome(s: str) -> bool:
        s2= s.replace(" ","")
        pattern = r'[^a-zA-Z0-9]'
        s1 = re.sub(pattern, '', s2)   
        i=0
        j=len(s1)-1
        while i < j:
            if s1[i].lower()!= s1[j].lower():                              
                return False
            else:
                i=i+1
                j=j-1
                continue                          
        return True
                        
                        

print(isPalindrome("Was it a car or as cat I saw?"))
