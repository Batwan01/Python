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