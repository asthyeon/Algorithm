import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 개똥벌레 (3020)
 1. 개똥벌레는 장애물을 피하지 않고 파괴하면서 지나감
 2. 동굴의 첫 번째 장애물은 항상 석순, 그 다음 종유석과 석순이 번갈아 등장
[입력]
 1. N: 동굴의 길이, H: 동굴의 높이
 2. N개의 줄: 장애물의 크기가 순서대로 주어짐
[출력]
 1. 개똥벌레가 파괴해야 하는 장애물의 최솟값과 그러한 구간의 수를 출력
"""

"""
<풀이>
 1. 일단 풀어보기 -> 누적합 이용
 2. 높이에 따른 종유석 추가하기
"""

N, H = map(int, input().split())
# 석순 (높이 + 1 만큼 만들기)
stalagmite = [0] * (H + 2)
# 종유석 (높이 + 1 만큼 만들기)
stalactite = [0] * (H + 2)

# 높이에 해당하는 장애물 위치 추가
for i in range(N):
    obstacle = int(input())

    # 석순 추가 (정방향)
    if i % 2 == 0:
        stalagmite[obstacle] += 1

    # 종유석 추가 (역방향)
    else:
        stalactite[H - obstacle + 1] += 1

# 누적합
for j in range(1, H + 1):
    # 석순 누적 (위에서 아래로)
    stalagmite[H + 1 - j] += stalagmite[H + 1 - j + 1]
    # 종유석 누적 (아래에서 위로)
    stalactite[j] += stalactite[j - 1]

# 파괴해야 하는 장애물의 최솟값, 그러한 구간의 수
destroy = N
cnt = 0

for k in range(1, H + 1):
    # 이번에 파괴해야 할 장애물 수
    now_destroy = stalagmite[k] + stalactite[k]

    # 최소값 교체 및 카운트 초기화
    if destroy > now_destroy:
        destroy = now_destroy
        cnt = 0

    # 구간 카운트
    if destroy == now_destroy:
        cnt += 1

print(destroy, cnt)