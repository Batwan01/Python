ans_N = int(input())
answer = list(map(int, input().split()))
answer.sort()

com_N = int(input())
compar = list(map(int, input().split()))
check = sorted(compar)

count = 0
for num in answer:
    while count < com_N and check[count] < num:
        count+=1
    if check[count] == num:
        check[count] = -1
        count+=1

last = 0
for num in compar:
    last = 0
    for i in check:
        if num == i:
            last+=1
            continue
    if last == 0:
        print('1')
    else:
        print('0')



# samenums = []
# for i in answer:
#     for j in check:
#         if i == j:
#             samenums.append(i)
#         elif i<j:
#             break

# for i in samenums:
#     for j in range(len(compar)):
#         if i == compar[j]:
#             compar[j] = -1

# for i in range(len(compar)):
#     if compar[i] == -1:
#         compar[i] = 1
#     else:
#         compar[i] = 0

# for i in compar:
#     print(i)
