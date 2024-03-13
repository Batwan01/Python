a, b = input().split()
int_a = int("".join(reversed(a)))
int_b = int("".join(reversed(b)))

if int_a > int_b:
  print(int_a)
else:
  print(int_b)