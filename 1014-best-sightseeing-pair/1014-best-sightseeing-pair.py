class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans = 0
        aiplusi = values[0] + 0
        for j in range(1,len(values)):
            ans = max(ans,aiplusi + values[j]-j)
            aiplusi = max(aiplusi , values[j] + j)
        return ans                                                    