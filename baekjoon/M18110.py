import sys
input = sys.stdin.readline

def roundup(num):
    if num-int(num)>=0.5:
        return int(num) + 1
    else:
        return int(num)
    
N = int(input())
array = []
if N == 0:
    print(0)
else:
    for i in range(N):
        array.append(int(input()))

    array.sort()
    exc = roundup(N*0.15)
    sum = sum(array[exc:len(array)-exc])
    if sum == 0:
        print(0)
    else:
        print(roundup(sum/(N-(exc*2))))