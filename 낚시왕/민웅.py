# 17143_낚시왕_fishing-master
import sys
input = sys.stdin.readline
dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def get_shark(column, sharks_field):
    point = 0
    for i in range(R):
        if sharks_field[i][column]:
            point = sharks_field[i][column][2]
            sharks_field[i][column] = 0
            break

    return point, sharks_field


def move_shark(sharks_field):
    shark_tmp = []
    for i in range(R):
        for j in range(C):
            if sharks_field[i][j]:
                S, D, Z = sharks_field[i][j]
                if D in [1, 2]:
                    S = S%(2*R-2)
                else:
                    S = S%(2*C-2)
                nx, ny = i, j
                dx, dy = dxy[D-1]
                for _ in range(S):
                    if not (0 <= nx + dx <= R-1) or not (0 <= ny + dy <= C-1):
                        if D in [1, 2]:  # 상하 반전
                            D = 3 - D
                        else:  # 좌우 반전
                            D = 7 - D
                        dx, dy = dxy[D-1]
                    nx, ny = nx + dx, ny + dy

                sharks_field[i][j] = 0
                # print(i, j, nx, ny)
                shark_tmp.append([nx, ny, S, D, Z])

    for sh in shark_tmp:
        r, c, s, d, z = sh
        if sharks_field[r][c]:
            if z > sharks_field[r][c][2]:
                sharks_field[r][c] = [s, d, z]
        else:
            sharks_field[r][c] = [s, d, z]

    return sharks_field


R, C, M = map(int, input().split())

field = [[0]*C for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    field[r-1][c-1] = [s, d, z]

master = 0
ans = 0
while True:
    if master == C:
        break

    p, field = get_shark(master, field)
    field = move_shark(field)
    ans += p
    master += 1

print(ans)
