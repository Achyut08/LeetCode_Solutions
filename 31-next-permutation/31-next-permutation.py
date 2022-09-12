class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        idx = -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                idx = i
                break
        if idx > -1:
            for i in range(len(nums)-1,-1,-1):
                if nums[i] > nums[idx]:
                    idx2 = i
                    break
            nums[idx],nums[idx2] = nums[idx2],nums[idx]
            l = idx+1
            r = len(nums)-1
            while (l<r):
                nums[l],nums[r] = nums[r],nums[l]
                l+= 1
                r -= 1
        else:
            nums.reverse()

    
    
    
    
#     Find the index of the first element which satisfies nums[i] < nums[i+1] : ind1
# Find the index of the first element which satisfies the condition nums[i] > nums[ind1] : ind2
# Swap nums[ind1] and nums[ind2]
# From the index ind1 to len(nums)-1 reverse the list
# If ind1 is not found, just reverse the list
# def nextPermutation(self, nums: List[int]) -> None:
#     """
#     Do not return anything, modify nums in-place instead.
#     """
#     ind1 = -1
#     for i in range(len(nums)-2,-1,-1):
#         if nums[i] < nums[i+1]:
#             ind1 = i
#             break
#     if ind1 > -1:
#         for i in range(len(nums)-1,-1,-1):
#             if nums[i]>nums[ind1]:
#                 ind2 = i
#                 break
#         nums[ind1],nums[ind2] = nums[ind2],nums[ind1]
#         l,r = ind1+1,len(nums)-1
#         while(l<r):
#             nums[l],nums[r] = nums[r],nums[l]
#             l+=1
#             r-=1
#     else:
#         nums.reverse()