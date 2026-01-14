class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slide_set = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in slide_set:
                slide_set.remove(s[l])
                l+=1
            slide_set.add(s[r])
            res = max(res,r-l+1)
        return res
