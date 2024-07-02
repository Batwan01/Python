num = int(input())

count = 0
for i in range(0,num):
    count+=pow(num-i,2)

print(count)