class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count = Counter(arr)
        nums = sorted(count)
        res = 0
        
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                curr = nums[i] + nums[l] + nums[r]
                if curr < target: l += 1
                elif curr > target: r -= 1
                else:
                    res += (count[nums[i]] *
                            count[nums[l]] *
                            count[nums[r]])
                    l += 1
                    r -= 1
        
        for n in nums:
            sub, m = divmod((target - n), 2)
            k = count[sub]
            if not m and k >= 2 and n != sub:
                res += (count[n] *
                        factorial(k) //
                        factorial(2) //
                        factorial(k - 2))
            if target == 3 * n and count[n] >= 3:
                k = count[n]
                res += (factorial(k) //
                        factorial(3) //
                        factorial(k - 3))
        
        return res % (10 ** 9 + 7)