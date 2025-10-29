class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        first = strs[0]
        d = {}
        min_len = min(len(s) for s in strs)
        
        for i in range(min_len):
            char = first[i]
            in_all = True
            for s in strs:
                if s[i] != char:
                    in_all = False
                    break
            
            if in_all:
                d[i] = char  # Store position and character
            else:
                break  # Stop at first mismatch
        
        # Build the prefix string from the dictionary
        s = ''
        for i in sorted(d.keys()):  # Sort by position to maintain order
            s += d[i]
        
        return s
