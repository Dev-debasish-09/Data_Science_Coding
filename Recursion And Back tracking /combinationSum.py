class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        combi = []
        self.getallcombination(candidates, 0, target, ans, combi)
        return ans

    def getallcombination(self, arr, index, target, ans, combin):
        # Base cases
        if target < 0:
            return
        if target == 0:
            ans.append(combin.copy())
            return
        if index == len(arr):
            return
        
        # Include current element (multiple times allowed)
        combin.append(arr[index])
        self.getallcombination(arr, index, target - arr[index], ans, combin)  # Use same index for multiple inclusions
        
        # Exclude current element (move to next)
        combin.pop()
        self.getallcombination(arr, index + 1, target, ans, combin)  # Move to next index
