class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        ans=[]
        if finalSum%2 == 1:
            return []
        i =2
        sum1=0
        while((sum1+i)<=finalSum):
            ans.append(i)
            sum1+=i
            i += 2
        temp = finalSum - sum1
        ele = ans.pop() + temp
        ans.append(ele)
        return ans
         
            
            
            
            
            
            
            
            
            
  

    