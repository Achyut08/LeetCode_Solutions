class Solution:
    def calPoints(self, s: List[str]) -> int:
        p = []
        for i in s:
            if i == 'C':
                p.pop()
            elif i == 'D':
                p.append(2*p[-1])
            elif i == '+':
                p.append(p[-1]+p[-2])
            else:
                p.append(int(i))
        return sum(p)