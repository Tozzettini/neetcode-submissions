class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        # so I add all chars to dic and they have a value of how
        # many times they appear
        for char in s:
                count[char] = count.get(char,0) + 1 
        # ---
        # Iterate through each char in t
        # if 's' is in count[s]
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
        return True