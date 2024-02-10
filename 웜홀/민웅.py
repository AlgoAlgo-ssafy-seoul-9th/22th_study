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

