import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 싫은데요 (25916)
 1. 햄스터는 구멍을 막기 위해 정확히 그 크기만큼의 부피를 소모해야 함
 2. 햄스터의 부피는 M으로 정해져 있음
 3. 막는 모든 구멍은 연속되어야 함
[입력]
 1. N: 구멍 수, M: 햄스터의 최대 부피
 2. A: 구멍들의 크기
[출력]
 1. 구멍을 막는 데에 활용할 수 있는 최대 부피 출력
"""

"""
<풀이>
 1. 투 포인터
"""

N, M = map(int, input().split())
A = list(map(int, input().split()))

# 최대 부피
maximum = 0

# 투 포인터
start = 0
end = 0
now = 0
while start < N and end < N:
    # 현재 값이 M보다 작거나 같다면 구멍 추가
    if now <= M:
        now += A[end]
        end += 1
    # 현재 값이 M보다 크다면 구멍 줄이기
    else:
        now -= A[start]
        start += 1

    # 최대 부피 갱신
    if now <= M:
        maximum = max(maximum, now)

print(maximum)

