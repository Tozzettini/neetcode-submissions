class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for key, value in enumerate(nums):
            compliment = target - value    
            if compliment in dic:
                return [dic[compliment], key]
            dic[value] = key
        return [0,0]