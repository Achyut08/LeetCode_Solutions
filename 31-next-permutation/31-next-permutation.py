class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n=len(nums)
        k=n-2
        l=0
        while k>=0:
            if nums[k]<nums[k+1]:
                break
            k -= 1
            
        if k<0:
            s = 0 
            e= n-1 
            while s<=e:
                nums[s],nums[e] = nums[e],nums[s]
                s+=1 
                e-=1
            return nums
        else:
            l=n-1
            while l>k:
                if nums[l]>nums[k]:
                    break
                l -= 1
            nums[k],nums[l]=nums[l],nums[k]
            s = k+1 
            e = n-1 
            while s<=e:
                nums[s],nums[e] = nums[e],nums[s]
                s+=1 
                e-=1 
        return nums
     
        



        