#https://www.hackerrank.com/challenges/dynamic-array/problem?isFullScreen=true

a = input().split(' ')
n , q = [int(x) for x in a]
arr = [[] for _ in range(n)]
lastans = 0

def insert(x,y):
    global lastans
    arr[(x^lastans) % n].append(y)
    
def printnum(x,y):
    global lastans
    z = arr[(x^lastans) % n]
    lastans = z[y % len(z)]
    print(lastans)

for i in range(q):
    li = [int(e) for e in input().split(' ')]
    insert(li[1], li[2]) if li[0] == 1 else printnum(li[1], li[2])
    
    