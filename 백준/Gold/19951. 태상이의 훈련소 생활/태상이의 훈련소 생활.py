import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 태상이의 훈련소 생활 (19951)
 1. 연병장의 각 칸에 흙을 덮거나 파내는 조교의 지시를 한 번에 처리하기
[입력]
 1. N: 연병장 크기, M: 조교 수
 2. 둘째 줄: 연병장 정보
 3. M개의 줄: 각 조교의 지시
[출력]
 1. 연병장의 각 칸의 높이 출력
"""

"""
<풀이>
 1. 누적 합
 2.
[0, 0, 0, 0, 0]의 연병장에서
1번 ~ 3번 +2라고 할 때,
[2, 2, 2, 0, 0]이 결과값
그렇다면
[2, 0, 0, -2, 0]을 이용하여 변화량 변수를 이용해서 만들 수 있음
변화량에 처음 2가 들어가고, 계속 2가 늘어나다가, -2 부분에서 변화량이 0이 되므로 늘어나지 않음
"""

# 연병장 크기 N, 조교 수 M
N, M = map(int, input().split())
# 연병장 정보
ground = list(map(int, input().split()))
# 누적합
prefix_sum = [0] * (N + 1)
# 조교 지시
for _ in range(M):
    a, b, k = map(int, input().split())
    # 변화의 시작점에 k 값 넣기
    prefix_sum[a - 1] += k
    # 변화의 종료지점 다음에 반대 부호의 k 값 넣기
    prefix_sum[b] -= k

# 변화량
change = 0
for i in range(N):
    # 변화량 조정
    change += prefix_sum[i]
    # 연병장에 변화량 반영
    ground[i] += change

print(*ground)