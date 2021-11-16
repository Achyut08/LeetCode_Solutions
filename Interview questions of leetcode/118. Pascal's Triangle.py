class Solution:
    def generate(self, newrow: int) -> List[List[int]]:
        if newrow==1:
            pascle=[[1]]
        else:
            pascle=[[1],[1,1]]
            for i in range(newrow-2):
                new=[1]
                for j in range(len(pascle[-1])-1):
                    new.append(pascle[-1][j]+pascle[-1][j+1])
                new.append(1)
                pascle.append(new)
        return pascle
