import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 선수과목 (Prerequisite) (14567)
 1. 어떤 과목들은 선수과목이 있어 해당되는 모든 과목을 먼저 이수해야 해당 과목 이수 가능
 2. 한 학기에 들을 수 있는 과목 수에는 제한이 없음
 3. 모든 과목은 매 학기 항상 개설됨
[입력]
 1. N: 과목의 수, M: 선수 조건의 수
 2. M개의 줄: A번 과목이 B번 과목의 선수과목
[출력]
 1. 1번 과목부터 N번 과목까지 차례대로 최소 몇 학기에 이수할 수 있는 지 한 줄에 출력
"""

"""
<풀이>
 1. 일단 풀어보기 -> 위상 정렬
"""
from collections import deque


# 위상 정렬
def topology_sort(subjects, prerequisites):
    q = deque([])
    # 각 과목의 최소 학기 이수 수
    answer = [1] * (N + 1)

    # 선수과목이 없는 과목 인큐
    for start in range(1, N + 1):
        if prerequisites[start] == 0:
            q.append(start)

    while q:
        now = q.popleft()
        # 선수과목 탐색
        for new in subjects[now]:
            # 선수과목 수 하나 줄이기
            prerequisites[new] -= 1
            # 선수과목이 없다면 인큐 및 현재 정답 갱신
            if prerequisites[new] == 0:
                q.append(new)
                # 현재 과목의 최소 학기 이수 수 + 1
                answer[new] = answer[now] + 1

    return answer[1:]


N, M = map(int, input().split())
# 과목 입력 및 각 과목의 선수과목 수
subjects = [[] for _ in range(N + 1)]
prerequisites = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, input().split())
    subjects[A].append(B)
    prerequisites[B] += 1

print(*topology_sort(subjects, prerequisites))