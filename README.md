# 22th_study

<br/>

# 이번주 스터디 문제

<details markdown="1" open>
<summary>접기/펼치기</summary>

<br/>

## [웜홀](https://www.acmicpc.net/problem/1865)

### [민웅](./웜홀/민웅.py)

```py


```

### [병국](./웜홀/병국.py)

```py


```

### [상미](./웜홀/상미.py)

```py

```

### [성구](./웜홀/성구.py)

```py


```

### [승우](./웜홀/승우.py)

```py


```

<br/>

## [낚시왕](https://www.acmicpc.net/problem/17143)

### [민웅](./낚시왕/민웅.py)

```py


```

### [병국](./낚시왕/병국.py)

```py


```

### [상미](./낚시왕/상미.py)

```py

```

### [성구](./낚시왕/성구.py)

```py


```

### [승우](./낚시왕/승우.py)

```py


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



</details>
