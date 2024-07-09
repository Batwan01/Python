def solution(board, h, w):
    n_h = len(board)
    n_w = len(board[0])
    count = 0
    dh, dw = [0,1,-1,0], [1,0,0,-1]
    color = board[h][w]
    for i, j in zip(dh,dw):
        if i+h<n_h and j+w<n_w and i+h>=0 and j+w>=0:
            if board[h+i][w+j] == color:
                count+=1
    return count