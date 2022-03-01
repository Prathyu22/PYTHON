#https://www.hackerrank.com/challenges/2d-array/problem?isFullScreen=true

def hourglass(arr):
    maxsum = -63
    
    for i in range(4):
        for j in range(4):
            top = sum(arr[i][j:j+3])
            mid = arr[i+1][j+1]
            bottom = sum(arr[i+2][j:j+3])
            
            hourglasssum = top+mid+bottom
            if hourglasssum > maxsum:
                maxsum = hourglasssum
    return maxsum

arr = []
for _ in range(6):
        arr.append(list(map(int, input().rstrip().split(' '))))

result = hourglass(arr)
print(result)

