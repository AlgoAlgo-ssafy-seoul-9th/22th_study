import sys, heapq
input = sys.stdin.readline


def bfs(si:int, sj:int, ei:int, ej:int) -> int:
    que = []
    heapq.heappush(que, (0, si, sj))
    visited= [[0] * N for _ in range(N)]
    visited[si][sj] = 1
    ans = -1
    while que:
        cost, i, j = heapq.heappop(que)
        if i == ei and j == ej:
            ans = cost
            break
        for di, dj in direction:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                visited[ni][nj] = 1
                heapq.heappush(que, (cost+1, ni, nj))
    return ans


N = int(input())
si, sj, ei, ej = map(int, input().split())
direction = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]
print(bfs(si-1, sj-1, ei-1, ej-1))