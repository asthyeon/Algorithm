import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 루머 (19538)
 1. 최초 유포자(여러 명 가능)를 제외하고 스스로 루머를 만들어 믿는 사람은 없음
 2. 매분 루머를 믿는 사람은 모든 주변인에게 루머를 동시에 퍼트림
 3. 군중 속 사람은 주변인의 절반 이상이 루머를 믿을 때 본인도 루머를 믿음
 4. 사람들이 루머를 처음 믿기 시작하는 시간 알아내기
[입력]
 1. N: 사람의 수
 2. N개의 줄: i번 사람의 주변인들의 번호와 입력의 마지막을 나타내는 0이 주어짐
 3. M: 최초 유포자의 수
 4. 마지막 줄: 최초 유포자의 번호들
[출력]
 1. 각 번호의 사람들이 루머를 처음 믿기 시작한 시간 출력
 2. 많은 시간이 지나도 루머를 믿지 않을 경우 -1, 최초 유포자는 0분부터 믿기 시작
"""

"""
<풀이>
 1. bfs
"""
from collections import deque


def bfs(people, spreaders, trusted):
    q = deque([])

    # 최초 유포자 선정 및 인큐
    for spreader in spreaders:
        trusted[spreader] = 0
        q.append(spreader)

    while q:
        now = q.popleft()

        # 주변인 탐색
        for new in people[now]:
            # 주변인 1명 믿음 -> 감소
            cnt[new] -= 1
            
            # 과반 수의 주변인이 믿고, 감염된 상태가 아니라면 
            if cnt[new] <= 0 and trusted[new] == -1:
                # 인큐 및 감염(이전 감염자의 +1 분)
                q.append(new)
                trusted[new] = trusted[now] + 1


N = int(input())
# 주변인 정보
people = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    around = list(map(int, input().split()))

    # 0번이 아닌 경우 i번 사람의 주변인 정보 입력
    for person in around:
        if person == 0:
            continue
        people[i].append(person)

M = int(input())
spreaders = list(map(int, input().split()))

# 루머를 믿는 사람들과 각 사람들이 몇명의 주변인이 믿어야 하는 지에 대한 숫자
trusted = [-1] * (N + 1)
cnt = [0] * (N + 1)

# 주변인 계산
for j in range(1, N + 1):
    cnt[j] = (len(people[j]) + 1) // 2

bfs(people, spreaders, trusted)

print(*trusted[1:])