N = int(input())

num=0
if N%5>2:
    num = N//5
    if (N-(num*5))%3 != 0:
        if N%3==0:
            print(N//3)
        else:
            print(-1)
    else:
        num = num + (N-(num*5))//3
        print(num)
elif N%3==0:
    print(N//3)
else:
    print(-1)