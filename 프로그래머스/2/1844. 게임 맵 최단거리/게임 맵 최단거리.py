from collections import deque
def solution(maps):
    H, W = len(maps), len(maps[0])
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    queue = deque([(0, 0, 1)])
    visited = [[False] * W for _ in range(H)]
    visited[0][0] = True
    
    while queue:
        x, y, count = queue.popleft()
        
        if x == H -1 and y == W - 1:
            return count
        
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            
            if 0 <= nx < H and 0 <= ny < W and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, count + 1))
    return -1