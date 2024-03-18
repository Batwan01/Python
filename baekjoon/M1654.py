N, K = map(int, input().split())
array = []

for _ in range(N):
    array.append(int(input()))

if K == 1:
    print(max(array))
    exit()

left = 1
right = max(array)

while left <= right:
    mid = (left + right) // 2
    count = sum(a // mid for a in array)

    if count >= K:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)
