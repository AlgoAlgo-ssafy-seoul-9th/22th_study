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


