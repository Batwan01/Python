import sys
input = sys.stdin.readline

T = int(input())
check = 0
for i in range(T):
    N, M = map(int,input().split())
    array = list(map(int, input().split()))
    
    while True:
        if array[check] < max(array[check:]):
            array.append(array[check])
            del array[check]
            check=0
        else:
            check+=1
        
        if check == len(array):
            check = 0   
            print(array)
            break
