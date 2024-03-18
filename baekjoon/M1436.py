N = int(input())
count = 0
i = 0
while True:
    i+=1
    str_i = str(i)
    len_i = len(str_i)
    for j in range(len_i):
        if len_i>j+2 and str_i[j] == '6':
            if str_i[j+1]=='6' and str_i[j+2]=='6':
                count+=1
                break
    if count == N:
        print(i)
        break