#포매팅

"hello my name is {}\n".format("jiwan")

a="jiwan"
b="korean"
"i'm {1} and {0}".format(a,b)

"{0:>10}".format("hi")
"{0:<10}".format("hi")
"{0:^10}".format("hi")

names='jiwan'
age=23
f'나의 이름은 {names}이고, 나이는 {age}입니다.'

#문자열

a="hobby"
a.count('b')
a.find('y') #존재하지 않으면 -1 반환

",".join("abcd") #a,b,c,d

a="hi"
a.upper() #"HI"
a.lower() #"hi"

a="  hi    "
a.lstrip() #왼쪽 공백 제거
a.rstrip() #오른쪽 공백 제거

a = "Life is too short"
a.split()

b = "a:b:c:d"
b.split(':')

#리스트

a=[1,2,['a', 'b', 'c']]
a[2] #['a', 'b', 'c']
a[2][0] #'a'

a=[1,2,3,4,5]
a1=a[:2]
a2=a[3:]
a1 #[1, 2]
a2 #[4, 5]

a=[1,2,3]
b=[3,4,5]
a+b #[1, 2, 3, 3, 4, 5]
a*3 #[1, 2, 3, 1, 2, 3, 1, 2, 3]
len(a) #3
del a[1] #1위치 값 제거
a #[1, 3]

a=[1,2,3]
str(a[2]) + "hi" #3hi
a.append(4) #뒤에 값 추가
a #[1, 2, 3, 4]

a=[1,5,7,6,3]
a.sort()
a #[1, 3, 5, 6, 7]
a.reverse()
a #[7, 6, 5, 3, 1]

a=[1,2,3]
a.index(3) #2 위치 알려주는 것
a.index(1) #0

a.insert(0,4)
a #[4, 1, 2, 3]

a.remove(4) #첫 번째로 나오는 4제거
a #[1, 2, 3]

a.pop() #리스트 마지막 값 출력 후 제거
a #[1, 2]
a.pop(1)
a #[1]
a.append(1) #[1, 1]
a.count(1) #1의개수 -> 2

del a[2:]
a.extend([2,3]) #리스트에 2,3추가 a+=[2,3]랑 같음
a #[1, 1, 2, 3]
a+=[2]
a #[1, 1, 2, 3, 2]