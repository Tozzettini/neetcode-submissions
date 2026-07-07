class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for index,value in enumerate(nums):

            count = target - value
            # if my target value is inside the list ()
            if count in dic:
                # issue
                # that means that the index()
                return [  dic.get(count), index ]
            dic[value] = index
        return [0,0]