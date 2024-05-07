N = int(input())
count = 0
num = 0
ori = N
flag = False
answer = 0
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
     for i in range(1,count):
          count-=1  
          N+=5
          if N%3 == 0:
               count+=N//3
               print(count)
               flag = True
               break
     if ori%3 == 0 and flag == False:
          print(ori//3)
     elif flag == False:
          print(-1)
elif flag == False:
     print(-1)