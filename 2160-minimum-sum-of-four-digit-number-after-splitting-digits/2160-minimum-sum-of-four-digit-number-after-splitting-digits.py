class Solution:
    def minimumSum(self, num: int) -> int:
        list1=[]
        for i in str(num):
            list1.append(i)
        list1.sort()
        print(list1)
        return int(str(list1[0] + list1[2])) +int(str(list1[1] + list1[3]))
        
        
        
        
        
        
#            num = sorted([i for i in list(str(num))])
#         return int(str(num[0] + num[2])) + int(str(num[1] + num[3]))