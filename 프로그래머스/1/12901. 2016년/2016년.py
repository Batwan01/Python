#a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴
#2월은 29일까지
def solution(a, b):
    dict_day = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    dict_month = {3:"SUN",4:"MON",5:"TUE",6:"WED",7:"THU",1:"FRI",2:"SAT"}
    day = 0
    answer = ""
    for mon in range(1,a):
        day+=int(dict_day[mon])
    day = (day+b)%7 if (day+b)%7!=0 else 7
    answer = dict_month[day]
    return answer
