import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 나의 인생에는 수학과 함께 (17265)
 1. 세현이네 집에서 학교까지 갈 때 숫자와 연산자의 결과값이 최대, 최소 구하기
[입력]
 1. N: 지도의 크기
 2. N개의 줄: 숫자와 연산자가 빈 칸을 사이에 두고 주어짐
[출력]
 1. 최댓값과 최솟값
"""

"""
<풀이>
 1. dfs
"""
import operator

# 연산자 변환용
changer = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}


# dfs (배열, x좌표, y좌표, 현재 값, 이전 연산자)
def dfs(arr, x, y, value, oper):
    global maximum, minimum

    # 도착지에 도달했을 때 값 갱신
    if x == N - 1 and y == N - 1:
        maximum = max(maximum, value)
        minimum = min(minimum, value)
        return

    # 델타탐색
    for dx, dy in [(0, 1), (1, 0)]:
        nx, ny = x + dx, y + dy

        # 범위 설정
        if 0 <= nx < N and 0 <= ny < N:
            # 숫자라면 값 연산
            if arr[nx][ny].isdigit():
                # 연산 후, value 갱신 및 oper 초기화
                dfs(arr, nx, ny, changer[oper](int(value), int(arr[nx][ny])), '')
            # 연산자라면 연산자 저장
            else:
                dfs(arr, nx, ny, value, arr[nx][ny])


N = int(input())
arr = [list(map(str, input().split())) for _ in range(N)]

# 최댓값과 최솟값
maximum = -10e9
minimum = 10e9

# dfs 탐색
dfs(arr, 0, 0, arr[0][0], '')

print(maximum, minimum)