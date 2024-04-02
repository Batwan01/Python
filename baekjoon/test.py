from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))
    queue = deque([(i, p) for i, p in enumerate(priority)])  # 문서의 인덱스와 중요도를 저장하는 deque
    print(queue)
    count = 0
    while True:
        current_doc = queue.popleft()  # 큐의 가장 왼쪽에 있는 문서를 가져옴
        if any(current_doc[1] < doc[1] for doc in queue):  # 중요도가 높은 문서가 있는지 확인
            queue.append(current_doc)  # 다른 문서가 중요도가 높으면 현재 문서를 큐의 맨 뒤로 이동
        else:
            count += 1  # 현재 문서를 출력
            if current_doc[0] == M:  # 찾고 있는 문서가 출력되었을 경우 반복문 종료
                print(count)
                break
