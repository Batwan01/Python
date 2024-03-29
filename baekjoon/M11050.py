import sys
input = sys.stdin.readline

def facotrial(N):
    result = 1
    for i in range(2,N+1):
        result *= i
    return result

N, K = map(int, input().split())
if N==K:
    print(1)
else:
    print(int(facotrial(N)/(facotrial(K)*facotrial(N-K))))