# "aya", "ye", "woo", "ma" 네 가지 발음, 조합만 가능
def solution(babbling):
    dict = {"aya":"1", "ye":"2", "woo":"3", "ma":"4"}
    count = 0
    ar = []
    for ch in babbling:
        before = ""
        check = False
        arr = []
        word = ch
        for dic in dict:
            word = word.replace(dic,dict[dic])
            
        if word.isdigit():
            for ch_word in word:
                if ch_word == before:
                    check = True
                    break
                before = ch_word
            if check == False: count+=1
    return count