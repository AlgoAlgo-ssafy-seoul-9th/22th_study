import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
sx, sy, ex, ey = map(int, input().split())
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

visited = [[False] * n for _ in range(n)]
visited[sx - 1][sy - 1] = True

queue = deque([(sx - 1, sy - 1, 0)])
minCnt = 10000000

while queue:
    tx, ty, cnt = queue.popleft()

    if (tx, ty) == (ex - 1, ey - 1):
        if cnt <= minCnt:
            minCnt = cnt
            
    for i in range(8):
        nx, ny = tx + dx[i], ty + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            visited[nx][ny] = True
            queue.append((nx, ny, cnt + 1))

if minCnt == 10000000:
    print(-1)
else:
    print(minCnt)