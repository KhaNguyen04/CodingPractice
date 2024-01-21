class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # BINARY SEARCH
        # Any peak will lie in a sorted sequence
        # ->if right num of 
        l,r=0,len(nums)-1
        while l<r:
            m=l+(r-l)//2
            if nums[m]>nums[m+1]:
                r=m
            else:
                l=m+1
        return r



        # LINEAR SCAN
        
        # i=0
        # stack=[]
        # for i in range(len(nums)):
        #     if stack and nums[i]<nums[stack[-1]]:
        #         return stack[-1]
        #     stack.append(i)
        # return stack[-1]