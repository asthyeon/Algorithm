import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 꿀 따기 (21758)
 1. N개의 장소 중 두 곳을 골라 벌을, 한 곳을 골라 벌통 두기
 2. 벌들을 벌통을 향해 날아가며 모든 칸에서 꿀을 땀
  - 두 마리가 모두 지나간 장소에서는 모두 표시된 양 만큼의 꿀을 땀(벌통 있는 곳도 동일)
  - 벌이 시작한 장소에서는 어떤 벌도 꿀을 딸 수 없음
[입력]
 1. N: 장소의 수
 2. 각 장소에 대한 꿀 양
[출력]
 1. 벌이 딸 수 있는 최대 꿀 양
"""

"""
<풀이>
 1. 누적합
 2. 누적합을 미리 구해놓고 벌통과 벌들의 위치를 이동시키며 계산
"""

N = int(input())
honeys = list(map(int, input().split()))

# 누적합 계산
prefix_sum = []
for i in range(N):
    if i == 0:
        prefix_sum.append(honeys[i])
    else:
        prefix_sum.append(prefix_sum[i - 1] + honeys[i])

# 최대 값
maximum = 0

# 벌통이 맨 왼쪽일 때
for left in range(1, N - 1):
    # 벌 하나는 계속 이동, 벌 하나는 맨 오른쪽
    maximum = max(maximum,
                  prefix_sum[left - 1] - honeys[left] +
                  prefix_sum[N - 2])

# 벌통이 맨 오른쪽일 때
for right in range(1, N - 1):
    # 벌 하나는 계속 이동, 벌 하나는 맨 왼쪽
    maximum = max(maximum,
                  prefix_sum[N - 1] - prefix_sum[right] +
                  prefix_sum[N - 1] - honeys[0] - honeys[right])

# 벌통이 안에 있을 때
for inner in range(1, N - 1):
    # 벌 하나는 맨 왼쪽, 벌 하나는 맨 오른쪽 = 1 ~ N - 2 까지의 합 + 벌통 반복
    maximum = max(maximum,
                  prefix_sum[N - 2] - honeys[0] + honeys[inner])

print(maximum)










