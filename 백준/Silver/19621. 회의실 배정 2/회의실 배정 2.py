import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 회의실 배정 2(19621)
 1. N개의 회의와 하나의 회의실
 2. 각 회의는 시작 시간, 끝나는 시간, 회의 인원이 주어지고 동시에 두 개 이상 회의 진행 불가
 3. 한 회의가 끝나야 다음 회의 시작 가능
[입력]
 1. N: 회의 수
 2. 시작시간, 끝나는 시간, 회의 인원
[출력]
 1. 회의실에서 회의를 진행할 수 있는 최대 인원 출력
"""

"""
<풀이>
 1. bfs
"""


# bfs
def bfs(conferences, completed, previous, total):
    global answer
    completed = set(completed)

    # 이전에 진행된 부분부터 시작하기
    for now in range(previous, N):
        # 처음일 땐 바로 집어넣기
        if not len(completed):
            bfs(conferences, list(completed) + [now], now, total + conferences[now][2])

        # 이미 진행된 회의라면 넘기기
        if now in completed:
            continue

        # 이번 회의가 이전 회의의 시작 시간보다 크거나 같다면 재귀
        if conferences[previous][1] <= conferences[now][0]:
            bfs(conferences, list(completed) + [now], now, total + conferences[now][2])
    
    # print(list(completed), previous, total)
    answer = max(answer, total)


# 회의 수 N
N = int(input())
# 각 회의 정보
conferences = []
for _ in range(N):
    # 회의 시작 시간, 끝나는 시간, 인원 수
    start, end, members = map(int, input().split())

    conferences.append((start, end, members))
conferences.sort()

# 정답
answer = 0
bfs(conferences, [], 0, 0)

print(answer)