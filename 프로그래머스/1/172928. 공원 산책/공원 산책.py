def solution(park, routes):
    answer = []
    direction = {
        "E": (0,1),
        "W": (0,-1),
        "S": (1,0),
        "N": (-1,0)
    }
    
    H, W = len(park), len(park[0])

    # i: 세로, j: 가로
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S': 
                x, y = i, j
                break 

    for route in routes:
        op, n = route.split()
        n = int(n)
        if x + direction[op][0] * n >= 0 and x + direction[op][0] * n < H and y + direction[op][1] * n >= 0 and y + direction[op][1] * n < W:
            xs, ys = x, y
            for _ in range(n):
                if park[x + direction[op][0]][y + direction[op][1]] != 'X':
                    x, y = x + direction[op][0], y + direction[op][1]
                else:
                    x, y = xs, ys
                    break
            
    return x,y