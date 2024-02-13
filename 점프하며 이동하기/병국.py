n = int(input())
r1,c1,r2,c2 = map(int,input().split())


direction = [(-1,-2),(1,-2),(-2,-1),(-2,1),(2,1),(2,-1),(1,2),(-1,2)]

# arr = [[0]*n for _ in range(n)]
v = [[0]*n for _ in range(n)]


q = [(r1-1,c1-1,0)]
# arr[r1-1][c1-1] = 1
v[r1-1][c1-1] = 1


flag = False
answer = -1
while q:
    x,y,cnt = q.pop(0)
    if x == r2-1 and y == c2-1:
        flag = True
        answer = cnt
        break
    for dx,dy in direction:
        nx = x+dx
        ny = y+dy
        if 0<=nx<n and 0<=ny<n and v[nx][ny] == 0:
            v[nx][ny] = 1
            q.append((nx,ny,cnt+1))
print(answer)