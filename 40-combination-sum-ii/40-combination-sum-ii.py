class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        self.output = []
        self.backtracking([],0,candidates,target)
        return self.output
    def backtracking(self,subset,start,candidates,target):
        if target == 0:
            self.output.append(list(subset))
        for i in range(start,len(candidates)):
            if candidates[i] > target:
                break
            if i != start and candidates[i] == candidates[i-1]:
                continue
            subset.append(candidates[i])
            self.backtracking(subset,i+1,candidates,target - candidates[i])
            subset.pop()