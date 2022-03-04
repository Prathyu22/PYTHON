#https://leetcode.com/problems/rotate-array/submissions/

class Solution(object):
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        le =len(nums)
        l, r = 0, le-1
        while l<r:
            nums[l],nums[r] = nums[r],nums[l]
            l,r = l+1,r-1
    
        l,r = 0,k-1
        while l<r:
            nums[l],nums[r] = nums[r],nums[l]
            l,r = l+1,r-1
    
        l,r=k,le-1
        while l<r:
            nums[l],nums[r] = nums[r],nums[l]
            l,r = l+1,r-1
        