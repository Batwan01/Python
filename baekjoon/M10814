'''
N(반복횟수)를 정한다.
for문을 통해
age, name을 입력한다.
age 순으로 sort -> name 순으로 sort한다.
'''

N = int(input())
answer = []

for i in range(N):
    [age_in, name_in] = map(str,input().split())
    answer.append([int(age_in), name_in])

answer.sort(key=lambda x: x[0])

for i in answer:
    print(i[0], i[1])
