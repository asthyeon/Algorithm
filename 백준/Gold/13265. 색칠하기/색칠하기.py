import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 색칠하기 (13265)
 1. 여러 동그라미를 그리는데 연결된 동그라미는 서로 색이 다르도록 칠하기
 2. 2가지 색상으로 색칠이 가능한 지 여부 파악하기
[입력]
 1. T: 테스트 케이스 개수
 2. n: 동그라미 개수, m: 직선들의 개수
 3. m개의 줄: 동그라미들이 연결된 직선에 대한 정보가 주어짐 (x, y)
[출력]
 1. 각 테스트 케이스에 대해 가능하면 possible, 불가느하면 impossible 출력
"""

"""
<풀이>
 1. bfs
"""
from collections import deque


# bfs
def bfs(start):
    # 시작 색은 검정 및 인큐
    visited[start] = 'black'
    q = deque([(start, 'black')])

    while q:
        now, color = q.popleft()

        # 인접 동그라미 탐색
        for new in circles[now]:
            if not visited[new]:
                # 현재의 색상에 따라 반대색상 부여
                if color == 'black':
                    visited[new] = 'white'
                    q.append((new, 'white'))
                else:
                    visited[new] = 'black'
                    q.append((new, 'black'))


# 색상 탐색하기
def explore(start):
    # 현재 색상과 연결된 색상 중 같은 색상이 있다면 False 종료
    for new in circles[start]:
        if visited[new] == visited[start]:
            return False
    # 모든 색상이 잘 연결되어 있다면 True 종료
    return True


T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())

    # 동그라미 연결
    circles = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        circles[x].append(y)
        circles[y].append(x)

    # 방문 리스트
    visited = [0] * (n + 1)
    # 1번부터 동그라미 색칠
    for start in range(1, n + 1):
        if not visited[start]:
            bfs(start)

    # 색상 탐색
    for start in range(1, n + 1):
        flag = explore(start)

        # False 일 경우 불가능
        if not flag:
            print('impossible')
            break
    # 모두 통과할 경우 가능
    else:
        print('possible')
