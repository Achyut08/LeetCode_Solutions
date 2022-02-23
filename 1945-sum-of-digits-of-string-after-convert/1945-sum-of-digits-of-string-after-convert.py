class Solution:
    def getLucky(self, s: str, k: int) -> int:
        s = "".join(str(ord(ch) - 96) for ch in s)
        for _ in range(k): 
            x = sum(int(ch) for ch in s)
            s = str(x)
        return x 