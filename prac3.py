money = True
if money:
    print("택시를 탄다")
else:
    print("걸어간다")

a = 5
print("a의 값은 %d" %a)

number = 0
prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number:
"""
while number != 4:
    print(prompt)
    number = int(input())

for i in range(2,10):
    for j in range(1,10):
        print(i*j, end = " ")
    print('')

a = [1,2,3,4]
result = [num*3 for num in a]
print(result)

result = [x*y for x in range(2,10)
          for y in range(1,10)]
print(result)

#3의 배수 구하기
result = 0
i = 0
while i<=1000:
    i += 1
    if i%3==0:
        result+=i
print(result)

#*탑 쌓기
for i in range(1,6):
    print("*"*i)

#1~100 출력
for i in range(1,101):
    print(i)

print([' '.join(str(i) for i in range(1,101))])

#점수 평균 구하기
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
for i in A:
    sum += i
print(sum/len(A))

#리스트 중 홀수에만 2를 곱하기
numbers = [1, 2, 3, 4, 5]
result = []
for i in numbers:
    if i%2!=0:
        result.append(i*2)
print(result)

#내포를 사용
numbers = [1, 2, 3, 4, 5]
result = [i*2 for i in numbers if i%2!=0]
print(result)

def add(a,b):
    return a+b
print(add(a=2,b=3))

def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

print(add_many(5,4,2))

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add', 1,2,3,4,5)
print(result)

result = add_mul('mul', 1,2,3,4,5)
print(result)

def add_and_mul(a,b):
    return a+b, a*b

a1, a2 = add_and_mul(2,3)
print(a1,a2)

a=1
def vartest(a):
    a = a + 1
    return a
print(vartest(a))

add = lambda a, b: a+b
result = add(3, 4)
print(result)
