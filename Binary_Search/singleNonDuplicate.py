class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        if nums[0]!= nums[1]:
            return nums[0]
        if nums[n-2] != nums[n-1]:
            return nums[n-1]
        
        start,end = 0,n-2
        while start <= end :
            mid = start+(end-start)//2
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            if (mid%2 == 0 and nums[mid] == nums[mid+1] or (mid % 2 == 1 and nums[mid] == nums[mid-1]) ):
                start = mid+1
            else:
                end = mid-1
        return -1

            
        
