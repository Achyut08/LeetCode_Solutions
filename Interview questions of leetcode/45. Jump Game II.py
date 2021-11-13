class Solution:
    
    def jump(self, nums: List[int]) -> int:
        current_max=0
        current_reach=0
        jump=0
        for i in range(len(nums)-1):
            if (nums[i]+i > current_max):
                current_max=nums[i]+i
            if ( i==current_reach):
                jump += 1
                current_reach=current_max
        return jump
