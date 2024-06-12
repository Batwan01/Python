#학교 학생 3명의 정수 번호를 더했을 때 0이 되면 3명의 학생은 삼총사
#5명의 학생이 있고, 각각의 정수 번호가 순서대로 -2, 3, 0, 2, -5
#첫 번째, 세 번째, 네 번째 학생의 정수 번호를 더하면 0이므로 세 학생은 삼총사
#두 번째, 네 번째, 다섯 번째 학생의 정수 번호를 더해도 0이므로 세 학생도 삼총사
def solution(number):
    count=0
    for i in range(len(number)-2):
        for j in range(i+1,len(number)-1):
            for h in range(j+1,len(number)):
                if number[i] + number[j] + number[h] == 0:
                    count+=1
    return count