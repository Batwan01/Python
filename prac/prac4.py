class FourCal:
  def __init__(self, first, second):
    self.first = first
    self.second = second
  def setdata(self, first, second):
    self.first = first
    self.second = second

a = FourCal(5,3)
a.firsts = 4
a.second = 3
print(a.first)
print(a.second)

class MoreFourCal(FourCal):
	pass

b = MoreFourCal(4,3)
print(b.first)

print(b.first ** b.second) #제곱

#mod1.py
def add(a, b):
	return a+b

def sub(a, b):
	return a-b

import mod1
print(mod1.add(1,2)) #3

from mod1 import add
add(3,4) #7

from mod1 import add,sub #add, sub함수 사용

from mod1 import * #mod1의 함수 모두 사용
