import sys
input = sys.stdin.readline
from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    array = list(map(int, input().split()))
    array = deque([(i, p) for i, p in enumerate(array)])  # 문서의 인덱스와 중요도를 저장하는 deque

    count = 0
    while array:
        current_doc = array.popleft()
        if any(current_doc[1] < doc[1] for doc in array):
            array.append(current_doc)
        else:
            count += 1
            if current_doc[0] == M:
                print(count)
                break