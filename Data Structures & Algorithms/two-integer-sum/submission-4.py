class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Need to create a dictionary that saves 
        # the indices and the value and that subtracts
        # and if the target is reached we can return the target
        dic = {}
        # initilize the dic and get each index and value in nums
        for key,value in enumerate(nums):
            # start adding values to dic
            compliment = target - value
            if compliment in dic:
                return [dic[compliment], key]
            dic[value] = key
        return [0,0]
            