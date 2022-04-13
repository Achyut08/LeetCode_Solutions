class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dict = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        def str_to_num(num):
            int_num = 0
            power = 1
            for i in range(len(num)):
                int_num += power*dict[num[-1-i]]
                power *= 10
            return int_num
    
        num1_int = str_to_num(num1)
        num2_int = str_to_num(num2) 
    
        mult_int = num1_int*num2_int
    
        return str(mult_int)