from collections import deque

def solution(players, callings):
    dict = {}
    
    for i, player in enumerate(players):
        dict[player] = i   
        
    for call in callings:
        idx = dict[call]
        
        players[idx], players[idx-1] = players[idx-1], players[idx]

        dict[players[idx]] = idx
        dict[players[idx-1]] = idx-1
    return players