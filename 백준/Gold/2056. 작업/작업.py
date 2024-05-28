import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 작업 (2056)
 1. 선행 관계: 어떤 작업을 수행하기 전 머저 완료되어야 할 작업들 관계
 2. K번 작업에 대한 선행 관계 작업들: 1 이상 K - 1 이하
 3. 선행 관계에 있는 작업이 하나도 없는 작업이 반드시 하나 이상 존재 (1번은 항상)
 4. 선행 관계가 없는 작업들은 동시 수행 가능
[입력]
 1. N: 수행해야 할 작업 수
 2. N개의 줄
  - 처음: 해당 작업에 걸리는 시간
  - 그 다음: 그 작업에 대해 선행 관계에 있는 작업들의 개수
  - 그 다음: 선행 관계에 있는 작업들의 번호
[출력]
 1. 모든 작업을 완료하기 위한 최소 시간 출력
"""

"""
<풀이>
 1. 동시 실행 가능 -> 각 작업을 수행하기 위해 필요한 이전 시간 + 해당 작업 시간
"""

N = int(input())

# 각 작업에 대한 소요 시간
times = {}
# 선행 작업
preceding = {}

for i in range(1, N + 1):
    work = list(map(int, input().split()))

    # 작업 시간 기록
    times[i] = work[0]
    # 선행 작업 기록
    preceding[i] = work[2:]

# 가장 오래걸리는 시간
answer = 0
# 작업 순회
for j in range(1, N + 1):

    # 가장 많이 걸리는 시간
    time = 0
    # 선행 작업 순회
    for pre in preceding[j]:
        # 가장 시간이 많이 걸리는 작업 찾기
        time = max(time, times[pre])

    # 현재 작업시간에 누적
    times[j] += time

    # 가장 오래 걸리는 시간 찾기
    answer = max(answer, times[j])

print(answer)