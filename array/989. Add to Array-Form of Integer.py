class Solution:
    def addToArrayForm(self, nums: List[int], k: int) -> List[int]:
        str1=""
        for i in nums:
            str1 += str(i)
        a=int(str1)+k
        res=[]
        for x in str(a):
            res.append(int(x))
        return res
