import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 여왕벌 (10836)
 1. 모든 애벌레들이 N일 동안 성장
 2. 하루에 0, 1, 2 성장
 3. 애벌레가 자라는 정도를 결정하는 규칙
  ㄱ. 제일 왼쪽 열, 제일 위쪽 행은 입력으로 주어짐
  ㄴ. 자라는 정도를 왼쪽 제일 아래칸부터 위쪽으로
  ㄷ. 제일 위쪽 칸에 도착하면, 오른쪽으로 가면서 행의 끝까지 읽음
  ㄹ. 모든 입력에서 이렇게 읽은 값들은 감소하지 않는 형태
  ㅁ. 나머지 애벌레들은 자신의 상하좌우가 다 자란 다음,
      가장 많이 자란 만큼 자신도 자람
[입력]
 1. M: 가로 세로 크기, N: 날짜 수
 2. 첫 날 아침의 애벌레 크기는 모두 1이므로 입력에 주어지지 않음
 3. N개의 줄: 0의 개수, 1의 개수, 2의 개수
[출력]
 1. M개의 줄에 각각 M개의 자연수 출력(애벌레 성장도)
"""

"""
<풀이>
 1. 일단 풀어보기
 2. 입력 값으로 주어지는 애들만 미리 성장 -> 나머지는 큰 값 따라가기
"""

M, N = map(int, input().split())
# 애벌레들
larvae = [[1] * M for _ in range(M)]
for _ in range(N):
    zero, one, two = map(int, input().split())

    # 성장해야 할 좌표
    x = M - 1
    y = 0
    # 맨 왼쪽 열과 맨 위쪽 행만 성장
    for n in range(2 * M - 1):
        # 성장도 0
        if zero:
            if not x:
                y += 1
            else:
                x -= 1
            zero -= 1
        # 성장도 1
        elif one:
            larvae[x][y] += 1
            if not x:
                y += 1
            else:
                x -= 1
            one -= 1
        # 성장도 2
        else:
            larvae[x][y] += 2
            if not x:
                y += 1
            else:
                x -= 1
            two -= 1

# 애벌레 성장도 출력
for x in range(M):
    for y in range(M):
        # 맨 위쪽 행
        if x == 0:
            print(larvae[x][y], end=" ")
        else:
            # 맨 왼쪽 열
            if y == 0:
                print(larvae[x][y], end=" ")
            # 그 외
            else:
                # 더 큰 값 따라가기
                print(max(larvae[x][0], larvae[0][y]), end=" ")
    print()

