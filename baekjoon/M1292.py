A, B = map(int,input().split())
sum = 0

result = []
for i in range(1, 1000):
    result.extend([i] * i)

for i in range(A-1, B):
    sum+=result[i]

print(sum)
