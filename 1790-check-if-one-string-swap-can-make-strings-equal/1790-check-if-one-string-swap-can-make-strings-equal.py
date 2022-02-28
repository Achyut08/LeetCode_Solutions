class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2 :
            return True
            
        ind = []
        for i in range(len(s1)) :
            if s1[i] != s2[i] :
                ind.append(i)
            if len(ind) > 2 :
                return False
        print(ind)
        print(s1[ind[0]])
        return ( s1[ind[0]] == s2[ind[-1]] ) and ( s1[ind[-1]] == s2[ind[0]] )