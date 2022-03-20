#https://www.interviewbit.com/problems/hotel-bookings-possible/

class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        arr = 0
        dep = 0
        c = 0
        ans = True
        arrive.sort()
        depart.sort()
        while(arr<len(arrive)):
            if(arrive[arr]<depart[dep]):
                arr += 1
                c += 1
            elif(arrive[arr]>depart[dep]):
                dep += 1
                c -= 1
            else:
                dep += 1
                arr += 1
            if(c>K):
                ans = False
                return ans

        return ans