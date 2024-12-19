import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 피자 오븐 (19940)
 1. 오븐 버튼 동작
  - ADDH: t + 60
  - ADDT: t + 10
  - MINT: t - 10
  - ADDO: t + 1
  - MINO: t - 1
 2. 오븐의 첫 시간은 0분, 0분보다 작아져도 0분으로 설정
[입력]
 1. T: 테스트 케이스 수
 2. N: 설정해야 하는 시간
[출력]
 1. 최소 횟수로 누르는 방법을 각각의 버튼 5개의 정수를 한 줄에 공백으로 구분해서 출력
"""

"""
<풀이>
 1. bfs -> 시간초과
 2. 시간을 나눠서 보기
 3. 뒤에서부터 누르기 (사전순)
"""
from collections import deque

# 버튼들
buttons = [60, 10, -10, 1, -1]


def bfs(N):
    # 60분 초과시 미리 누르기
    q = deque([(0, N // 60, 0, 0, 0, 0)])
    N %= 60
    used = [0] * 61

    while q:
        time, ADDH, ADDT, MINT, ADDO, MINO = q.popleft()

        # 설정 시간일 경우 종료
        if time == N:
            return ADDH, ADDT, MINT, ADDO, MINO

        # 중복 처리
        if not used[time]:
            used[time] = 1
            # 버튼 누르기(사전순)
            for button in range(4, -1, -1):
                new = time + buttons[button]

                # 0 미만 초기화
                new = max(new, 0)
                # 60분 초과는 60으로 초기화
                new = min(new, 60)

                # 버튼 횟수 증가
                cnts = [ADDH, ADDT, MINT, ADDO, MINO]
                cnts[button] += 1
                q.append((new, cnts[0], cnts[1], cnts[2], cnts[3], cnts[4]))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    print(*bfs(N))