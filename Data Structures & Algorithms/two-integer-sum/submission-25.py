class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # check if the list is empty
        
        dic = {}
        for index, value in enumerate(nums):
            compliment = target - value
            if compliment in dic:
                return [ dic.get(compliment), index ]
            dic[value] = index
        return [0,0]