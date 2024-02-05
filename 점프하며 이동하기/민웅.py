import sys
from collections import deque
input = sys.stdin.readline

dxy = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]

N = int(input())

r1, c1, r2, c2 = map(int, input().split())
r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1

field = [[0]*N for _ in range(N)]
ans = -1

q = deque()
field[r1][c1] = 1
q.append([r1, c1, 0])

while q:
    x, y, cnt = q.popleft()
    if x == r2 and y == c2:
        ans = cnt
        break

    for d in dxy:
        nx = x + d[0]
        ny = y + d[1]

        if 0 <= nx <= N-1 and 0 <= ny <= N-1:
            if not field[nx][ny]:
                q.append([nx, ny, cnt+1])
                field[nx][ny] = 1
print(ans)