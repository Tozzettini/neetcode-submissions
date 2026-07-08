class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len (t):
            return False
        dic = {}
        for value in s:
            dic[value] = dic.get(value, 0) + 1

        for value in t:
            
            if value not in dic or dic[value] <= 0:
                return False

            dic[value] -= 1
               
            
        return True