import sys
input = sys.stdin.readline

deq = []
instr = []
N = int(input())

for i in range(N):
    instr = list(map(str,input().split()))

    if instr[0] == 'push_front':
        deq.insert(0, instr[1])
    elif instr[0] == 'push_back':
        deq.append(instr[1])
    elif instr[0] == 'pop_front':
        if len(deq) != 0:
            print(deq.pop(0))
        else:
            print('-1')
    elif instr[0] == 'pop_back':
        if len(deq) != 0:
            print(deq.pop())
        else:
            print('-1')
    elif instr[0] == 'size':
        print(len(deq))
    elif instr[0] == 'empty':
        if len(deq) != 0:
            print(0)
        else:
            print('1')
    elif instr[0] == 'front':
        if len(deq) != 0:
            print(deq[0])
        else:
            print('-1')
    elif instr[0] == 'back':
        if len(deq) != 0:
            print(deq[-1])
        else:
            print('-1')
