arr = [[1,2],[3,4]]
arr1 = [[5,6],[7,8]]
answer = [[],[]]
count = 0
for num1,num2 in arr,arr1:
    for n1, n2 in num1,num2:
        answer[count].append(n1+n2)
    count+=1
print(answer)