A, B, V = map(int, input().split())

days = (V - B) / (A - B)

if days != int(days):
    days = int(days) + 1
else:
    days = int(days)

print(days)