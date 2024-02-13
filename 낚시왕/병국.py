import sys
input = sys.stdin.readline
def move_shark():
    new_sea = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            x = i
            y = j
            # 상어있으면 이동
            if sea[i][j] != 0:
                direction = [sea[i][j][1]]
                dx = direction[0][0]
                dy = direction[0][1]
                # 속력만큼 갈거임
                # print(sea[i][j])
                for k in range(sea[i][j][0]):
                    nx = x + dx
                    ny = y + dy
                    # 범위 안에 있으면
                    if 0<=nx<R and 0<=ny<C:
                        pass
                    # 범위 넘어가면
                    else:
                        # 방향바꾸고
                        dx = -dx
                        dy = -dy
                    x += dx
                    y += dy
                # print(x,y,dx,dy)
                # 이미 있으면 크기비교
                if new_sea[x][y] != 0:
                    if new_sea[x][y][2] < sea[i][j][2]:
                        new_sea[x][y] = (sea[i][j][0],(dx,dy),sea[i][j][2])
                else:
                    new_sea[x][y] = (sea[i][j][0], (dx, dy), sea[i][j][2])
    return new_sea



dir = [(-1,0),(1,0),(0,1),(0,-1)]

R,C,M = map(int,input().split())
sea = [[0]*C for _ in range(R)]
for _ in range(M):
    # r,c 위치, s 속력, d 방향, z 크기
    r,c,s,d,z = map(int,input().split())
    r -= 1
    c -= 1
    d -= 1
    # print(d)
    sea[r][c] = [s,dir[d],z]

# 총 C초동안 이동함
# 상어 잡고
# 상어 움직인다.
answer = 0
for i in range(C):
    # i 열에 있는 상어부터 잡기
    for j in range(R):
        # 상어가 있으면
        if sea[j][i] != 0:
            # 크기만큼 더해
            answer += sea[j][i][2]
            sea[j][i] = 0
            break
    sea = move_shark()
    # print(sea)
print(answer)