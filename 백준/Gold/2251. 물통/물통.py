import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 물통(2251)
 1. A, B, C 세 물통
 2. A, B는 비어 있고, C는 가득 차 있음
 3. 다른 물통으로 부을 때 한 물통이 비거나 다른 물통이 가득 찰 때까지 부을 수 있음
[입력]
 1. 세 물통의 용량 A, B, C가 주어짐(1 <= A, B, C <= 200)
[출력]
 1. A가 비었을 때 C에 담겨있을 수 있는 물의 양을 오름차순으로 구하기
"""

"""
<풀이>
 1. bfs
 2. 각 경우의 수 다 구해보기
  - a + b > B
  - [a + b - B][B]
  - a + b <= B
  - [a - a][b + a]
  - 변수: b - B or -a = B - b or a
"""
from collections import deque


# bfs
def bfs(A, B, C):
    # 가장 큰 물병 크기
    size = max(A, B, C) + 1
    # 각 물병들의 상태 조합의 기록
    bottles = [[[0] * size for _ in range(size)] for _ in range(size)]
    # 정답 세트
    answers = set()
    # 처음 상태 인큐 및 상태 기록
    q = deque([(0, 0, C)])
    bottles[0][0][C] = 1
    answers.add(C)

    while q:
        a, b, c = q.popleft()

        # A -> B로 채우기
        # 물이 넘치는지 안넘치는지에 따라 값 설정
        A_to_B = min(B - b, a)
        # 기록된 상태가 아니라면 기록
        if not bottles[a - A_to_B][b + A_to_B][c]:
            bottles[a - A_to_B][b + A_to_B][c] = 1
            q.append((a - A_to_B, b + A_to_B, c))
            # 정답이라면 기록
            if a - A_to_B == 0:
                answers.add(c)

        # A -> C로 채우기
        # 물이 넘치는지 안넘치는지에 따라 값 설정
        A_to_C = min(C - c, a)
        # 기록된 상태가 아니라면 기록
        if not bottles[a - A_to_C][b][c + A_to_C]:
            bottles[a - A_to_C][b][c + A_to_C] = 1
            q.append((a - A_to_C, b, c + A_to_C))
            # 정답이라면 기록
            if a - A_to_C == 0:
                answers.add(c + A_to_C)

        # B -> A로 채우기
        # 물이 넘치는지 안넘치는지에 따라 값 설정
        B_to_A = min(A - a, b)
        # 기록된 상태가 아니라면 기록
        if not bottles[a + B_to_A][b - B_to_A][c]:
            bottles[a + B_to_A][b - B_to_A][c] = 1
            q.append((a + B_to_A, b - B_to_A, c))
            # 정답이라면 기록
            if a + B_to_A == 0:
                answers.add(c)

        # B -> C로 채우기
        # 물이 넘치는지 안넘치는지에 따라 값 설정
        B_to_C = min(C - c, b)
        # 기록된 상태가 아니라면 기록
        if not bottles[a][b - B_to_C][c + B_to_C]:
            bottles[a][b - B_to_C][c + B_to_C] = 1
            q.append((a, b - B_to_C, c + B_to_C))
            # 정답이라면 기록
            if a == 0:
                answers.add(c + B_to_C)

        # C -> A로 채우기
        # 물이 넘치는지 안넘치는지에 따라 값 설정
        C_to_A = min(A - a, c)
        # 기록된 상태가 아니라면 기록
        if not bottles[a + C_to_A][b][c - C_to_A]:
            bottles[a + C_to_A][b][c - C_to_A] = 1
            q.append((a + C_to_A, b, c - C_to_A))
            # 정답이라면 기록
            if a + C_to_A == 0:
                answers.add(c - C_to_A)

        # C -> B로 채우기
        # 물이 넘치는지 안넘치는지에 따라 값 설정
        C_to_B = min(B - b, c)
        # 기록된 상태가 아니라면 기록
        if not bottles[a][b + C_to_B][c - C_to_B]:
            bottles[a][b + C_to_B][c - C_to_B] = 1
            q.append((a, b + C_to_B, c - C_to_B))
            # 정답이라면 기록
            if a == 0:
                answers.add(c - C_to_B)

    return sorted(answers)


# 각 물통의 용량 A, B, C
A, B, C = map(int, input().split())

print(*bfs(A, B, C))