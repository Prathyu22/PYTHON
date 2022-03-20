#https://leetcode.com/problems/find-peak-element/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        ''' --------------This running time is O(n)-------------------- '''
        #if first or last element is a peak element
        if(len(nums)==1):
            return 0
        elif(nums[0]>=nums[1]):
            return 0
        elif(nums[len(nums)-1]>=nums[len(nums)-2]):
            return len(nums)-1
        
        #for any other element in the array        
        for i in range(1,len(nums)):
            if (nums[i-1] < nums[i] and nums[i] > nums[i+1]) :
                return i
        
    ''' -------------For running in O(log n), use divide and conquer technique------------ '''