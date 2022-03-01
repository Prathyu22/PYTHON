#https://www.hackerrank.com/challenges/sparse-arrays/problem?isFullScreen=true

n = int(input())
strings = list()
results = list()

for i in range(0,n):
    strings.append(input())
    
q = int(input())   
for i in range(0,q):
    queries = input()
    count = 0
    for n in strings:
        if n == queries:
            count = count + 1
    results.append(count)
                
for count in results:
    print(count)
