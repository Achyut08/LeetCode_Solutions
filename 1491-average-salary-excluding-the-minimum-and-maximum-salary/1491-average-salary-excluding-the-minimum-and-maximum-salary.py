class Solution:
    def average(self, salary: List[int]) -> float:
        if len(salary) == 3:
            mini = min(salary)
            maxy = max(salary)
            return sum(salary) - (mini+maxy)
        mini = min(salary)
        maxy = max(salary)
        salary_sum = sum(salary) - (mini+maxy)
        return salary_sum/(len(salary)-2)