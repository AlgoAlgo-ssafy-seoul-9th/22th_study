def gogo(start):
    dis = [10001] * (n+1)
    dis[start] = 0

    # 노드만큼 돌릴건데
    for i in range(n):

        # 원래 한사이클 돌면 갱신이 다된다.
        for start,end,distance in road:
            if dis[end] > dis[start]+distance:
                dis[end] = dis[start]+distance
                # 근데 i == n-1 까지 갱신을 할 수 있다?
                # 사이클이 존재한다는 것
                if i == n-1:
                    return False
        # print(i,dis)
    return True


INF = float('inf')
tc = int(input())
for t in range(tc):
    n,m,w = map(int,input().split())
    road = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        road.append((s,e,t))
        road.append((e,s,t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        road.append((s,e,-t))
    # print(road)
    answer = gogo(1)
    # print(answer)
    if answer == False:
        print('YES')
    else:
        print('NO')
