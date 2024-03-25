N, K = map(int, input().split())

array = []
for i in range(1, N+1):
    array.append(i)

idx = 0
print('<', end='')
for i in range(N):
    idx = (idx + K -1) % len(array)
    print(array.pop(idx), end = '')
    if len(array) == 0:
        break
    else:
        print(end = ', ')
print('>')