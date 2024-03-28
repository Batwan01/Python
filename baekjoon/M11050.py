import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline
def facotrial(N):
    if N==1:
        return 1
    return N * facotrial(N-1)

N, K = map(int, input().split())

print(int(facotrial(N)/(facotrial(K)*facotrial(N-K))))