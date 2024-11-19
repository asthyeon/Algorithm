import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 줄 세우기 (2252)
 1. N명의 학생들을 키 순서대로 줄 세우려고 함
 2. 두 학생의 키를 비교하는 방법 사용
[입력]
 1. N: 학생 수, M: 키를 비교한 횟수
 2. M개의 줄: 학생 A가 학생 B의 앞에 서야 함
[출력]
 1. 학생들을 앞에서부터 줄을 세운 결과 출력
   (답이 여러 가지인 경우에는 아무거나 출력)
"""

"""
<풀이>
 1. 위상정렬
"""
from collections import deque


# 위상 정렬
def topology_sort(rank, students):
    # 큐 및 줄 세우기
    q = deque()
    line_up = []

    # 진입 차수가 0인 학생들 인큐 (가장 작은 학생들)
    for student in range(1, N + 1):
        if rank[student] == 0:
            q.append(student)

    while q:
        # 가장 작은 학생들부터 디큐 및 줄 세우기
        now = q.popleft()
        line_up.append(now)

        # 현재 학생보다 큰 학생 찾기
        for up in students[now]:
            # 큰 학생 차수 -1
            rank[up] -= 1
            # 진입 차수가 0인 경우 인큐
            if rank[up] == 0:
                q.append(up)

    return line_up


N, M = map(int, input().split())
# 학생 등급과 학생 리스트
rank = [0] * (N + 1)
students = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    # 더 작은 학생에 큰 학생을 붙이고 큰 학생 차수 올리기
    students[A].append(B)
    rank[B] += 1

print(*topology_sort(rank, students))