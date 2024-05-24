#n의 각 자릿수를 큰것부터 작은 순으로 정렬
#n이 118372면 873211을 리턴

def solution(n):
    list_num = [int(num) for num in list(map(int, reversed(sorted(str(n)))))]
    return int(''.join(map(str,list_num)))