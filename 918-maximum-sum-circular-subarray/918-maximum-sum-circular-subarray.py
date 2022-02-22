class Solution:
    def maxSubarraySumCircular(self, arr: List[int]) -> int:
        n  = len(arr)
        def normalmaxsum(nums,n):
            sums=0
            maximun=nums[0]
            for i in nums:
                if sums<0:
                    sums=0
                sums += i
                maximun=max(sums,maximun)
            return maximun
        def overallsum(arr,n):
            max_normal = normalmaxsum(arr,n)
            if max_normal < 0:
                return max_normal
            arr_sum = 0
            for i in range(n):
                arr_sum += arr[i]
                arr[i] = - arr[i]
            max_circular = arr_sum + normalmaxsum(arr,n)
            return max(max_normal,max_circular)
        ans = overallsum(arr,n)
        return ans