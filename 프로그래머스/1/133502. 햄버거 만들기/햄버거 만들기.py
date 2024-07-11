def solution(ingredient):
    word = []
    count = 0
    find = [1, 2, 3, 1]
    
    for num in ingredient:
        word.append(num)
        if word[-4:] == find:
            count += 1
            del word[-4:]
    
    return count

