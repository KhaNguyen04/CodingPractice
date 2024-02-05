class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store the compliment and its index
        dic={}
        for i in range(len(nums)):
            compliment=target-nums[i]
            if nums[i] not in dic:
                dic[compliment]=i
            else:
                return [dic[nums[i]],i]
