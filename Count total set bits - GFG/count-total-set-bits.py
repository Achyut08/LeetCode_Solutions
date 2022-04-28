#User function Template for python3

class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        
        n += 1; 

    # To store the powers of 2 
        powerOf2 = 2; 

    # To store the result, it is initialized 
    # with n/2 because the count of set 
    # least significant bits in the integers 
    # from 1 to n is n/2 
        cnt = n // 2; 

    # Loop for every bit required to represent n 
        while (powerOf2 <= n) :

        # Total count of pairs of 0s and 1s 
            totalPairs = n // powerOf2; 

        # totalPairs/2 gives the complete 
        # count of the pairs of 1s 
        # Multiplying it with the current power 
        # of 2 will give the count of 
        # 1s in the current bit 
            cnt += (totalPairs // 2) * powerOf2; 

        # If the count of pairs was odd then 
        # add the remaining 1s which could 
        # not be groupped together 
            if (totalPairs & 1) :
                cnt += (n % powerOf2)
            else :
                cnt += 0

        # Next power of 2 
            powerOf2 <<= 1; 

    # Return the result 
        return cnt; 
        # code here
        # return the count

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        ob=Solution()
        print(ob.countSetBits(int(input())))
# } Driver Code Ends