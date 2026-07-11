class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s.lower())
        new_array= []
        for i in s:
            if i.isalnum():
                new_array.append(i)

  
        l=0
        r=len(new_array)-1

        while l<=r:
            if new_array[l] != new_array[r]:
                return False
            else:
                r-=1
                l+=1
        return True