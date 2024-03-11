N, M = map(int,input().split())

array = list(range(N+1))
for i in range(M):
  A, B = map(int, input().split())
  Bigger = A if A>B else B
  Smaller = A if A<B else B

  array[Smaller:Bigger+1] = reversed(array[Smaller:Bigger+1])

print(*array[1:])