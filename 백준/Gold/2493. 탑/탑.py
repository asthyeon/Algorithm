import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 탑 (2493)
 1. 모든 탑의 레이저는 왼쪽 방향으로 발사
 2. 하나의 탑에서 발사된 신호는 가장 먼저 만나는 하나의 탑에서만 수신이 가능
 3. 탑의 크기가 더 커야 수신 가능(높이가 같은 탑은 존재 X)
[입력]
 1. N: 탑의 수
 2. 두번째 줄: 탑들의 높이가 직선상에 놓인 순서대로 주어짐
[출력]
 1. 각 탑들의 신호를 몇 번의 탑이 수신 받는 지 출력(수신하는 탑이 존재하지 않으면 0)
"""

"""
<풀이>
 1. 일단 풀어보기 -> 시간 초과
 2. 스택, 역순으로 풀기
"""

N = int(input())
towers = list(map(int, input().split()))

stack = []
answer = []
for i in range(N):
    # 스택이 들어있다면
    while stack:
        # 스택의 마지막 높이와 현재 타워 높이 비교 
        if stack[-1][1] > towers[i]:
            # 현재 타워 높이가 더 작다면 가장 먼저 만나는 인덱스 번호 넣고 종료
            answer.append(stack[-1][0] + 1)
            break
        # 가장 먼저 만나는 타워가 더 작다면 그 다음 타워 탐색
        else:
            stack.pop()
    # 스택이 비어있다면 수신 가능한 탑이 존재 X
    if not stack:
        answer.append(0)
    # 스택 쌓기 (인덱스, 높이)
    stack.append((i, towers[i]))

print(*answer)