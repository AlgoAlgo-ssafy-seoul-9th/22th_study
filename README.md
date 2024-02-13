# 22th_study

<br/>

# 이번주 스터디 문제

<details markdown="1" open>
<summary>접기/펼치기</summary>

<br/>

## [웜홀](https://www.acmicpc.net/problem/1865)

### [민웅](./웜홀/민웅.py)

```py
# 1865_웜홀_Wormhole
import sys
input = sys.stdin.readline

def bellman_Ford(start):
    distance[start] = 0

    for i in range(1, N+1):
        for j in range(1, N+1):
            for node, cost in graph[j]:
                # if distance[j] != 10001:
                if distance[node] > distance[j] + cost:
                    distance[node] = distance[j] + cost
                    if i == N:
                        return True
    return False


T = int(input())

for tc in range(T):
    N, M, W = map(int, input().split())
    # S 시작지점, E 도착지점, T 도로이동시간, 줄어드는시간
    graph = [[] for _ in range(N+1)]
    distance = [10001]*(N+1)
    # print(distance)
    for i in range(M):
        S, E, T = map(int, input().split())
        graph[S].append([E, T])
        graph[E].append([S, T])
    for i in range(W):
        S, E, T = map(int, input().split())
        graph[S].append([E, -T])

    ans = bellman_Ford(1)
    # print(distance)
    if ans:
        print('YES')
    else:
        print('NO')


```

### [병국](./웜홀/병국.py)

```py


```

### [상미](./웜홀/상미.py)

```py

```

### [성구](./웜홀/성구.py)

```py
# 1865 웜홀
import sys
input = sys.stdin.readline

# 벨만 - 포드 알고리즘
def bellman_ford(N:int, M:int, graph:list):
    # 최댓값으로 초기화
    visited =[10_001*M] *(N+1)
    # 시작은 0
    visited[1] = 0
    # N번 탐색
    for i in range(N):
        # 노드 N 번 업데이트
        for node in graph:
            s, e, t = node
            if visited[e] > visited[s] + t:
                visited[e] = visited[s] + t
                # 마지막 N번째 업데이트 되면, 음의 값을 갖는다.
                # 음의 사이클 찾는 방법
                if i == N-1:
                    return "YES"
    # 음의 사이클 없음
    return "NO"

def solution():
    N, M, W = map(int, input().split())
    graph = []
    for _ in range(M):
        s,e,t = map(int, input().split())
        graph.append(tuple([s,e,t]))
        graph.append(tuple([e,s,t]))
    for _ in range(W):
        s,e,t = map(int, input().split())
        graph.append(tuple([s,e,-t]))
    print(bellman_ford(N, M, graph))
    return


if __name__ == "__main__":
    for _ in range(int(input())):
        solution()

```

### [승우](./웜홀/승우.py)

```py
import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

TC = int(input())
INF = 123456789

def bf(start):
    distance = [INF for _ in range(N + 1)]
    distance[start] = 0

    for i in range(N):
        for edge in edges:
            cur = edge[0]
            next = edge[1]
            cost = edge[2]

            if distance[next] > cost + distance[cur]:
                distance[next] = cost + distance[cur]

                if i == N - 1:
                    return True
    return False

for _ in range(TC):
    N, M, W = map(int, input().split())
    answer = False
    edges = list()
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append([S, E, T])
        edges.append([E, S, T])

    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append([S, E, -T])

    check = bf(1)
    if check:
        print("YES")
    else:
        print("NO")

```

<br/>

## [낚시왕](https://www.acmicpc.net/problem/17143)

### [민웅](./낚시왕/민웅.py)

```py
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

```

### [병국](./낚시왕/병국.py)

```py


```

### [상미](./낚시왕/상미.py)

```py

```

### [성구](./낚시왕/성구.py)

```py
# 17143 낚시왕
import sys
input = sys.stdin.readline
# 상어 움직임
def moving(R:int, C:int, M:int, ocean:list, sharks:list) -> None:
    # 움직인 상어들 저장용
    tmp = [[0] * (C+1) for _ in range(R+1)]
    # 상어 순서대로 움직임
    for i in range(1, M+1):
        # 이미 잡혔거나 먹혔으면 0
        if sharks[i] != 0:
            # 상어 정보
            r, c, s, d, z = sharks[i]
            # 움직임이 있는 애들만 실행
            if s != 0:
                # 방향별 설정
                if d == 1:      # 위
                    if s > r-1:
                        k = s-r+1
                        dir = 1
                        while k > R-1:
                            k -= R-1
                            dir += 1

                        if dir%2:
                            r = k+1
                            d = 2
                        else:
                            r = R-k
                    else:
                        r -= s

                elif d == 2:        # 아래
                    if s > R-r:
                        k = s-(R-r)
                        dir = 1
                        while k > R-1:
                            k -= R-1
                            dir += 1

                        if dir%2:
                            r = R-k
                            d = 1
                        else:
                            r = k+1

                    else:
                        r += s


                elif d == 3:        # 오른쪽
                    if s > C-c:
                        k = s-(C-c)
                        dir = 1
                        while k > C-1:
                            k -= C-1
                            dir += 1

                        if dir%2:
                            c = C-k
                            d = 4
                        else:
                            c = k+1

                    else:
                        c += s
                else:               # 왼쪽
                    if s > c-1:
                        k = s-(c-1)
                        dir = 1
                        while k > C-1:
                            k -= C-1
                            dir += 1

                        if dir%2:
                            c = k+1
                            d = 3
                        else:
                            c = C-k

                    else:
                        c -= s
            # 상어 정보 업데이트
            sharks[i] = (r, c, s, d, z)
            # 이미 자리에 상어가 있으면 더 큰 상어가 먹음
            if tmp[r][c]:
                if sharks[tmp[r][c]][4]<sharks[i][4]:
                    # 크면 먹어버리고
                    sharks[tmp[r][c]] = 0
                    tmp[r][c] = i
                else:
                    # 작으면 먹힘
                    sharks[i] = 0
            else:
                # 없을 땐 그냥 자리잡음
                tmp[r][c] = i
    # 상어 위치 업데이트
    for ni in range(1, R+1):
        for nj in range(1, C+1):
            ocean[ni][nj] = tmp[ni][nj]
    return


def solution():
    # 상어 정보 입력 받기
    for _ in range(M):
        # d 위 1, 아래 2, 오른쪽 3, 왼쪽 4
        sharks.append(tuple(map(int, input().split())))
    # 상어 정보를 바탕으로 바다에 풀기
    for i in range(1,M+1):
        r, c, s, d, z = sharks[i]
        ocean[r][c] = i
    # 최종 잡은 상어의 무게
    shark_sizes = 0
    # 낚시 시작
    for turn in range(1,C+1):       # 어부의 위치
        for i in range(1, R+1):         # 낚시 중
            if ocean[i][turn]:          # 상어가 있으면 바로 잡음
                shark_sizes += sharks[ocean[i][turn]][4]
                sharks[ocean[i][turn]] = 0
                ocean[i][turn] = 0
                break                   # 한 번 잡으면 상어 움직임
        # 상어 움직임 ㄱㄱ
        moving(R, C, M, ocean, sharks)
    print(shark_sizes)


if __name__ == "__main__":
    # 전역 설정을 통해 어디서든 가져다 쓸 수 있도록 설정
    R, C, M = map(int, input().split())
    ocean = [[0] * (C+1) for _ in range(R+1)]
    sharks = [0]
    solution()

```

### [승우](./낚시왕/승우.py)

```py
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
```

</details>

<br/><br/>

# 지난주 스터디 문제

<details markdown="1">
<summary>접기/펼치기</summary>

## [단어 삭제](https://www.codetree.ai/problems/word-delete/description)

### [민웅](./단어%20삭제/민웅.py)

```py
import sys
input = sys.stdin.readline


all_word = list(input().strip())

bomb = list(input().strip())
bl = len(bomb)
stack = []

for i in range(len(all_word)):
    stack.append(all_word[i])
    tmp = len(stack)
    if tmp >= bl and stack[-1] == bomb[-1]:
        if stack[tmp-bl:] == bomb:
            stack = stack[:tmp-bl]


print(*stack, sep='')
```

### [병국](./단어%20삭제/병국.py)

```py


```

### [상미](./단어%20삭제/상미.py)

```py
import sys
input = sys.stdin.readline

wordsList = input().strip()
word = input().strip()
l = len(word)   # 2
i = 0

while i + l <= len(wordsList):
    if wordsList[i:i+l] == word:
        wordsList = wordsList[:i] + wordsList[i+l:]
        i = 0
    else:
        i += 1
print(wordsList)

```

### [성구](./단어%20삭제/성구.py)

```py
import sys
input = sys.stdin.readline



string = list(input().strip())
delete = input().strip()

i = 0
while i < len(string):
    if string[i] == delete[0]:
        tmp = string[i:]
        for j in range(1, len(delete)):
            if tmp[j] != delete[j]:
                i += 1
                break
        else:
            string = string[:i]+string[i+len(delete):]
            i = max(0, i -len(delete)-1)
    else:
        i += 1
print("".join(string))

'''
import sys
input = sys.stdin.readline


s = input().strip()
p = input().strip()

while p in s:
    s = s.replace(p, "")
print(s)
'''

```

### [승우](./단어%20삭제/승우.py)

```py

```

## [점프하며 이동하기](https://www.codetree.ai/problems/move-while-jumping/description)

### [민웅](./점프하며%20이동하기/민웅.py)

```py
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

```

### [병국](./점프하며%20이동하기/병국.py)

```py


```

### [상미](./점프하며%20이동하기/상미.py)

```py
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
```

### [성구](./점프하며%20이동하기/성구.py)

```py
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
```

### [승우](./점프하며%20이동하기/승우.py)

```py

```

## [알파벳 조합](https://www.codetree.ai/problems/alphabet-combination/description)

### [민웅](./알파벳%20조합/민웅.py)

```py


```

### [병국](./알파벳%20조합/병국.py)

```py


```

### [상미](./알파벳%20조합/상미.py)

```py


```

### [성구](./알파벳%20조합/성구.py)

```py
import sys
input = sys.stdin.readline

def dfs():
    global ans, cnt
    if len(stack) == N:
        s = "".join(stack)
        if s not in ans:
            ans.add(s)
            print(s)
        if len(ans) >= 10_000:
            return 1
        return 0
    if len(ans) >= 10_000 or cnt >= 10_000:
        return 1

    for i in range(N):
        if not visited[i]:
            stack.append(arr[i])
            visited[i] = 1
            if dfs():
                return 1
            stack.pop()
            visited[i] = 0
    return 0

arr = sorted(list(input().strip()))
N = len(arr)
if len(set(arr)) == 1:
    print("".join(arr))
else:
    visited= [0] * N
    stack = []
    ans = set()
    cnt = 0
    dfs()

```

### [승우](./알파벳%20조합/승우.py)

```py


```

</details>

<br/><br/>

# 알고리즘 설명

<details markdown="1">
<summary>접기/펼치기</summary>

### [Bellman-Ford 정리 확인하기](https://coyote.tistory.com/2)

</details>
