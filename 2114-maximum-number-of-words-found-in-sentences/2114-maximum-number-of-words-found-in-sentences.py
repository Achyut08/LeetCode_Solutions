class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans1 = 0 
        for i in sentences:
            ans = len(i.split())
            ans1 = max(ans,ans1)
        return ans1
        
        	# return max(len(word.split()) for word in sentences)
