#https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # SET doesn't consists of duplicate elements.
        return [x for x in set(nums) if nums.count(x) > len(nums)/3]
    