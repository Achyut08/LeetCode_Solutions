class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 2:
            return nums

        even = sorted([nums[i] for i in range(0, n, 2)])
        print(even)
        odd = sorted([nums[i] for i in range(1, n, 2)], reverse=True)
        print(odd)
        res = []

        for i in range(len(even)):
            res.append(even[i])
            if i < len(odd):
                res.append(odd[i])

        return res