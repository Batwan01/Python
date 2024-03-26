from collections import deque

N = int(input())

que = deque()

for i in range(1,N+1):
    que.append(i)

while len(que) != 1:
    que.popleft()
    pop_n = que.popleft()
    que.append(pop_n)

print(que.pop())