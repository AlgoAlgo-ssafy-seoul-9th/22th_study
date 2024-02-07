import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())

cage = [[0 for _ in range(C + 1)] for _ in range(R + 1)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    cage[r][c] = [s, d, z]

answer = 0

for i in range(1, C + 1):

    for j in range(1, R + 1):
        if cage[j][i]:
            answer += cage[j][i][2]
            cage[j][i] = 0
            break
    
    new_cage = [[0 for _ in range(C + 1)] for _ in range(R + 1)]

    for j in range(1, R + 1):
        for k in range(1, C + 1):
            if cage[j][k]:
                s, d, z = cage[j][k]
                if d == 1:
                    row = j - s
                    col = k
                    while not (0 < row <= R):
                        d = 2 if d == 1 else 1
                        if row <= 0:
                            row = 2-row
                        else:
                            row = 2*R - row
                elif d == 2:
                    row = j + s
                    col = k
                    while not (0 < row <= R):
                        d = 2 if d == 1 else 1
                        if row <= 0:
                            row = 2-row
                        else:
                            row = 2*R - row
                elif d == 3:
                    row = j
                    col = k + s
                    while not (0 < col <= C):
                        d = 4 if d == 3 else 3
                        if col <= 0:
                            col = 2-col
                        else:
                            col = 2*C - col
                elif d == 4:
                    row = j
                    col = k - s
                    while not (0 < col <= C):
                        d = 4 if d == 3 else 3
                        if col <= 0:
                            col = 2-col
                        else:
                            col = 2*C - col
                
                if new_cage[row][col] == 0:
                    new_cage[row][col] = [s, d, z]
                else:
                    prev_z = new_cage[row][col][2]
                    new_cage[row][col] = [s, d, z] if z > prev_z else new_cage[row][col]

    cage = new_cage
                            
print(answer)
