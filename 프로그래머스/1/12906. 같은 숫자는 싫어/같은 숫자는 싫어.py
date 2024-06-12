#배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 
#배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거
#제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지
def solution(arr):
    count = 0
    answer = [arr[0]]
    for num in arr:
        if num == answer[count]:
            continue
        else:
            count+=1
            answer.append(num)
        
    return answer