import re

def dot_remove(answer):
    answer = answer[:-1] if answer and answer[-1] == '.' else answer
    answer = answer[1:] if answer and answer[0] == '.' else answer
    return answer

def solution(new_id):
    answer = ''
    
    answer = new_id.lower()
    answer = re.sub(r'[^a-z0-9-_.]', '', answer)
    answer = re.sub(r'\.+', '.', answer)
    
    answer = dot_remove(answer)
    
    answer = answer if answer else 'a'
        
    answer = answer[:15] if len(answer) >= 16 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer
    
    while len(answer) < 3:
        answer+=answer[-1]

    return answer