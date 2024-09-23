import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 도둑 (13422)
 1. 도둑은 연속된 집에서 돈을 훔칠 수 있음
 2. K원 이상 돈을 훔칠 경우 잡힘
[입력]
 1. T: 테스트 데이터 수
 2. N: 집의 개수, M: 돈을 훔칠 연속된 집의 개수, K: 방범 장치가 작동하는 최소 돈의 양
 3. 둘째 줄: N개의 집에서 각각 보관중인 돈의 양이 시계방향 순서대로 공백으로 주어짐
 4. 첫째 집과 마지막 집은 서로 연결되어 있음
[출력]
 1. M개의 집에서 돈을 훔치는 방법의 가짓수를 한 줄에 1개씩 출력
"""

"""
<풀이>
 1. 슬라이딩 윈도우
 2. 돈을 훔치는 방법의 가짓수는 돈의 양이므로 중복을 걸러야 함 -> X
 3. 돈을 훔치는 가짓수 자체가 중복이 되면 안됨
"""

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())

    houses = list(map(int, input().split()))
    # 개수가 똑같은 경우를 제외하고 M개의 집 잇기(처음 부분)
    if N - M != 0:
        houses += houses[:M - 1]

    # 집 길이 및 시작 돈, 훔치는 방법의 가짓수
    length = len(houses)
    money = sum(houses[:M])
    cnt = 0

    # 윈도우 시작과 끝
    start = 0
    end = M - 1
    while True:
        # 돈 훔치는 것이 가능한 경우
        if money < K:
            cnt += 1

        # 윈도우 이동
        money -= houses[start]
        start += 1
        end += 1
        # 종료 조건
        if end == length:
            break
        money += houses[end]

    print(cnt)

