N = int(input())
compare = input().split()

dict = {}
for element in compare:
    dict[element] = dict.get(element, 0) + 1

M = int(input())
have = input().split()

for i in have:
    print(dict.get(i,0), end = ' ')