#https://www.hackerrank.com/challenges/arrays-ds/problem?isFullScreen=true

n = int(input())
A = [int(x) for x in input().split(' ')]

'''print(A[::-1])''' # gives the output as array
# the below gives the output as values of the array.
A = A[::-1]

for x in A:
    print(x, end=' ')
