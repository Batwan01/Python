import sys
input = sys.stdin.readline
N = int(input())

que = []
instr = []
for i in range(N):
    instr = list(map(str, input().split()))

    if instr[0] == 'push':
        que.append(instr[1])
    elif instr[0] == 'pop':
        if len(que) == 0:
            print('-1') 
        else:
            print(que.pop(0))
    elif instr[0] == 'size':
            print(len(que))
    elif instr[0] == 'empty':
        if len(que) == 0:
            print('1') 
        else:
            print('0')
    elif instr[0] == 'front':
        if len(que) == 0:
            print('-1') 
        else:
            print(que[0])
    elif instr[0] == 'back':
        if len(que) == 0:
            print('-1') 
        else:
            print(que[-1])