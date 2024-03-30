import sys
input = sys.stdin.readline

for i in range(100):
    exc = round(i*0.15)
    if i-exc==0:
        print('i : ', i , 'exc : ', exc, 'sum : ', i-exc)