t1 = ()
t2 = (1,) #1개의 요소를 가지면 요소 뒤에 ,를 붙여야함
t3 = (1,2,3)
t4 = 1,2,3
t5 = ('a', 'b', ('ab', 'cd'))

t1 = (1,2,3)
t1[0] #1
t1[1:] #(2,3)
t2 = (3,4)
t1 + t2 #(1,2,3,2,3)
t2*3 #(3,4,3,4,3,4)
len(t1) #3

t1+t2

a = {1: 'hi'} #key = 1 , value = 'hi'
a = {'a': [1,2,3]} #value에 리스트 삽입 가능
a['name'] = 'jiwan' #name(Key) = jiwan(Value)
del a['name'] #name 키 삭제
a.keys()

s1=set("Hello")
s1

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
s1 & s2
s1 | s2
s2 - s1