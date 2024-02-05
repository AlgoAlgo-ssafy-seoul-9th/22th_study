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