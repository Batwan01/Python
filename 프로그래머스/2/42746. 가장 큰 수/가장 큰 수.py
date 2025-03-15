from functools import cmp_to_key

def solution(numbers):
    def compare(x, y):
        return (int(y + x) - int(x + y)) 

    sorted_numbers = sorted(map(str, numbers), key=cmp_to_key(compare))

    result = ''.join(sorted_numbers)
    
    return result if result[0] != '0' else '0'
