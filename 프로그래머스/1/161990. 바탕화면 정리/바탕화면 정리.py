from collections import defaultdict


def solution(wallpaper):
    lx, ly, rx, ry = 100, 100, -1, -1
    
    for i, line in enumerate(wallpaper):
        for j, ch in enumerate(line):
            if ch == '#':
                if i < lx:
                    lx = i
                if j < ly:
                    ly = j
                if i > rx:
                    rx = i
                if j > ry:
                    ry = j
                    
    return [lx, ly, rx+1, ry+1]