# 2시 32분 시작
#value는 세로 N, 가로 M 크기의 집터를 골랐다. 집터 맨 왼쪽 위의 좌표는 (0, 0)이다.
#우리의 목적은 이 집터 내의 땅의 높이를 일정하게 바꾸는 것

# 두 가지 작업이 가능하다.
# 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다. < 2초 걸림
# 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다. < 1초 걸림

# 최소 시간이랑 높이 구하기
# 작업을 시작할 때 인벤토리에는 B개의 블록이 들어 있다.
# 땅의 높이는 256블록을 초과할 수 없으며, 음수가 될 수 없다.

# 첫째 줄에 세로 N, 가로 M, 인벤토리 B가 주어진다
# 둘째 줄부터 N개의 줄에 각각 M개의 정수로 땅의 높이가 주어진다.
# (i + 2)번째 줄의 (j + 1)번째 수는 좌표 (i, j)에서의 땅의 높이를 나타낸다.
# 땅의 높이는 256보다 작거나 같은 자연수 또는 0이다.
import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
arr = []
for i in range(N):
    arr.extend(list(map(int, input().split())))

# 초기 통계 수집
max_height = max(arr)
min_height = min(arr)

# 블록 수를 기록할 배열
height_count = [0] * 257
for height in arr:
    height_count[height] += 1

# 최적의 높이와 시간을 초기화
min_time = float('inf')
best_height = 0

# 가능한 모든 높이 (min_height ~ max_height) 에 대해 반복
for target_height in range(min_height, max_height + 1):
    remove_blocks = 0
    add_blocks = 0
    for height in range(257):
        if height > target_height:
            remove_blocks += (height - target_height) * height_count[height]
        elif height < target_height:
            add_blocks += (target_height - height) * height_count[height]
    
    # 인벤토리에 있는 블록과 제거한 블록으로 충분히 채울 수 있는 경우
    if remove_blocks + B >= add_blocks:
        current_time = remove_blocks * 2 + add_blocks
        if current_time < min_time or (current_time == min_time and target_height > best_height):
            min_time = current_time
            best_height = target_height

print(min_time, best_height)
