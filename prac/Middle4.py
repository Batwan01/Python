file_name = "numbers.txt"

total = 0

with open(file_name, 'r') as file:
    for line in file:
        num = int(line.strip())
        total += num

print("정수 10개의 합:", total)
