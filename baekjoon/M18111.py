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

N, M, B = map(int,input().split())
SUM = 0
arr = []

for i in range(N):
    arr.extend(list(map(int, input().split())))

avg = round(sum(arr)/(N*M))
diff = [num - avg for num in arr]
diff_num = B + sum(num for num in diff if num<0)
print(diff)

if diff_num < 0:
    diff = [num-1 if num>0 else num+1 for num in diff]
    avg-=1
print(diff)
for num in diff:
    if num == 0:
        continue
    elif num > 0:
        SUM+=2*abs(num)
    else:
        SUM+=1

print(SUM, avg)