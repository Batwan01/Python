number = int(input())
start = 2
multi = 1
while True:
    if number == 1:
        print(1)
        break
    elif number in range(start,start+6*multi):
        print(multi+1)
        break
    else:
        start = start + 6*multi 
        multi+=1