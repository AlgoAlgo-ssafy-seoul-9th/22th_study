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
