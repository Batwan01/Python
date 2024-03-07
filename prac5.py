try:
  4/0
except ZeroDivisionError as e:
	print(e)

try:
  print("try 수행")
	#무엇가를 수행한다.
finally:
	print("finally 실행")
     
try:
  a = [1,2]
  print(a[3])
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

try:
  a = [1,2]
  print(a[3])
except (ZeroDivisionError, IndexError) as e:
    print(e)

class Bird:
    def fly(self):
      raise NotImplementedError
    
class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()

class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)
try:
  say_nick("천사")
  say_nick("바보")
except MyError:
  print("허용되지 않는 닉네임 입니다.")

import re
p = re.compile('[a-z]+')
m = p.match("3python")
print(m)

m = p.search("3python")
print(m)

result = p.findall("life is too short")
print(result)

p = re.compile('a.b', re.DOTALL)
m = p.match('a\nb')
print(m)

p = re.compile("^python\s\w+")
data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))

charref = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]);')

charref = re.compile(r"""
&[#]
(
  0[0-7]+
| [0-9]+
| x[0-9a-fA-F]          
)
;                     
""", re.VERBOSE)

p = re.compile(r"\w+\s+\d+[-]\d+[-]\d+")

p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(2))