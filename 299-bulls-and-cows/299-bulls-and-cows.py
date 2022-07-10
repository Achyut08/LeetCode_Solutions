class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows, d1, d2 = 0, 0, {}, {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            d1[secret[i]] = d1.get(secret[i], 0) + 1
            d2[guess[i]] = d2.get(guess[i], 0) + 1
        for k, val in d1.items():
            if k in d2:
                cows += min(val, d2[k])
        return f'{bulls}A{cows-bulls}B'