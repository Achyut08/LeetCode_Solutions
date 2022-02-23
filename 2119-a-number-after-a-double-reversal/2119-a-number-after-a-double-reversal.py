class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        str1 = str(num)
        print(str1[-1])
        if str1[-1] == "0":
            return False
        else:
            return True

    