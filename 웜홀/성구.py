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