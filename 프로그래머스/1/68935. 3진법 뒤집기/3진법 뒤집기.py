#n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현
def solution(n):
    num = n
    arr = []
    while num!=0:
        arr.append(num%3)
        num//=3
        
    total = 0
    count = len(arr)-1
    for num in arr:
        total += num * pow(3,count)
        count-=1
    return total

