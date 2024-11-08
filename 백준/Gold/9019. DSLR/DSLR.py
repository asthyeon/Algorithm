import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# DSLR (9019)
 1. D: n 을 두 배로 바꿈, 값이 9,999 보다 큰 경우 10,000 으로 나눈 나머지를 취하고 저장
 2. S: n 에서 1 을 뺀 결과 n - 1 을 레지스터에 저장, n 이 0 이라면 9,999 저장
 3. L: n 의 각 자릿수를 왼편으로 회전시켜 저장
 4. R: n 의 각 자릿수를 오른편으로 회전시켜 저장
 5. 두 정수 A 와 B 에 대하여, A 를 B 로 바꾸는 최소한의 명령어 생성하기
[입력]
 1. T: 테스트 케이스 수
 2. A, B
[출력]
 1. A 에서 B 로 변환하기 위해 필요한 최소한의 명령어 나열 출력
  - 가능한 명령어 나열이 여러가지면, 아무거나 출력
"""

"""
<풀이>
 1. 백트래킹 -> 재귀 초과
 2. bfs -> 시간초과 -> 숫자에 대한 방문 리스트를 만들기
"""
from collections import deque


def bfs(A, B):
    # 0 ~ 10,000 숫자 방문 리스트
    visited = [0] * 10001
    visited[A] = 1
    # 현재 숫자와 명령어가 들어간 큐
    q = deque([(A, '')])

    while q:
        now, command = q.popleft()

        # 정답인 경우 종료
        if now == B:
            return command

        # D 명령어
        D = now * 2 % 10000
        if not visited[D]:
            visited[D] = 1
            q.append((D, command + 'D'))

        # S 명령어
        S = now - 1
        if S < 0:
            S = 9999
        if not visited[S]:
            visited[S] = 1
            q.append((S, command + 'S'))

        # L 과 R 을 실행하기 위해 네 자리 문자로 치환
        now = f'{now:04d}'

        # L 명령어
        L = int(now[1] + now[2] + now[3] + now[0])
        if not visited[L]:
            visited[L] = 1
            q.append((L, command + 'L'))

        # R 명령어
        R = int(now[3] + now[0] + now[1] + now[2])
        if not visited[R]:
            visited[R] = 1
            q.append((R, command + 'R'))


T = int(input())
for tc in range(1, T + 1):
    A, B = map(int, input().split())

    print(bfs(A, B))