import random as r

count = 0
for i in range(1000):
    if r.randint(1, 6) == 2:
        count+=1


print("2가 나온 횟수 : ", count)
