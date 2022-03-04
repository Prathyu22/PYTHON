#https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        dict_ = Counter(nums)
        #print(dict_)
		
        # return the key with maximum value
        return max(dict_, key=dict_.get)
        