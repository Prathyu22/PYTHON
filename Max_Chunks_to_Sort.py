#https://leetcode.com/problems/max-chunks-to-make-sorted/submissions/

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_i = 0
        res = 0
        for i,v in enumerate(arr):
            max_i = max(max_i, v)
            if max_i == i:
                res += 1
        return res        