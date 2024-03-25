ans_N = int(input())
answer = set(map(int, input().split()))

com_N = int(input())
compar = list(map(int, input().split()))

for i in compar:
    if i in answer:
        print('1')
    else:   
        print('0')