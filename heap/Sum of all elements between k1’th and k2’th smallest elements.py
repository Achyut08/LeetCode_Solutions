def sumBetweenTwoKth(arr, n, k1, k2):
 
    # Sort the given array
    #go for heap function

    arr.sort()
 
    result = 0
    for i in range(k1, k2-1):
        result += arr[i]
    return result
 

 
 
