class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()   # sort to handle duplicates
        ans = []
        self.backtrack(candidates, 0, target, [], ans)
        return ans

    def backtrack(self, arr, index, target, path, ans):
        # valid combination found
        if target == 0:
            ans.append(path.copy())
            return
        
        # no more elements or target becomes negative
        if target < 0:
            return
        
        for i in range(index, len(arr)):
            # skip duplicates
            if i > index and arr[i] == arr[i - 1]:
                continue
            
            # pick the number
            path.append(arr[i])
            
            # move to next index (each element used only once)
            self.backtrack(arr, i + 1, target - arr[i], path, ans)
            
            # backtrack
            path.pop()
