array = list(range(1,31))
for i in range(28):
  array.remove(int(input()))

print(min(array))
print(max(array))