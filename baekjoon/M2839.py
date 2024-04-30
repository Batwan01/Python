N = int(input())
count = 0
num = 0
ori = N
flag = False
if N >= 5:
     count = N//5
     N = N % 5
     if N == 0:
          print(count)
          flag = True

if N%3==0 and flag == False:
     count += N//3
     print(count)
elif ori>=6 and flag == False:
     count-=1
     N+=5
     if N%3 == 0:
          count+=N//3
          print(count)
     else:
          print(-1)
elif flag == False:
     print(-1)