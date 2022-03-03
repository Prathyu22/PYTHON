#https://leetcode.com/problems/squares-of-a-sorted-array/submissions/

class Solution(object):
    def sortedSquares(self, arr):
        arr1 = []
        for i in range(len(arr)):
            arr1.append(arr[i]**2)

        return sorted(arr1)


