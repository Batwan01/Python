from collections import Counter

data = [1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4]

# Counter 객체 생성
counter = Counter(data)
print(counter)
# 가장 빈번하게 등장하는 요소들
most_common = counter.most_common()
print(most_common)

# 두 번째로 큰 등장 횟수 찾기
second_most_common = most_common

print("두 번째로 큰 등장 횟수:", second_most_common[0][1])
