word = []
count = 0
flag = True

while True:
    word.append(input())
    count += 1
    if word[0] == '.':
        break
    elif word[-1][-1] == '.':
        while True:
            stack = []
            if len(word) == 0:
                break
            words = word.pop(0)
            count -= 1
            for i in range(len(words)):
                if words[i] == '(' or words[i] == '[' or words[i] == '{':
                    stack.append(words[i])
                elif words[i] == ')' and len(stack) != 0:
                    if stack.pop() == '(':
                        continue
                    else:
                        print('no')
                        flag = False
                        break
                elif words[i] == '] and len(stack) != 0':
                    if stack.pop() == '[':
                        continue
                    else:
                        print('no')
                        flag = False
                        break
                elif words[i] == '}' and len(stack) != 0:
                    if stack.pop() == '{':
                        continue
                    else:
                        print('no')
                        flag = False
                        break
                else:
                    flag = False
                    print('no')
                    break
            if flag == True:
                print('yes')
            else:
                flag = True
    else:
        continue
