class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}

        for char in s:
            count[char] = count.get(char,0) + 1  
        # count[char] initilizes the key
        # count.get[char, 0], gets the key and adds 1 to it, if thers none default is 0
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
        return True