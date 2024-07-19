from collections import Counter

def solution(participant, completion):
    participant_counter = Counter(participant)
    completion_counter = Counter(completion)
    
    for participant in participant_counter:
        if participant_counter[participant] != completion_counter[participant]:
            return participant