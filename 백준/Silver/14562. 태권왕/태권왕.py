import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 태권왕
 1. 연속 발차기
  A: 현재 점수만큼 점수 얻고, 상대도 3득점
  B: 1점
 2. 태균이 점수 S점과 상대 점수 T점이 주어질 때 S와 T가 같아지는 최소 연속 발차기 수 구하기
[입력]
 1. C: 테스트 케이스 수
 2. C줄에 걸쳐 점수 S와 상대 점수 T
[출력]
 1. S와 T가 같아지는 최소 연속 발차기 횟수 출력
"""

"""
<풀이>
 1. 힙큐 사용
"""
import heapq


# 발차기
def kick(S, T):
    if S == T:
        return 0

    hq = [(0, S, T)]

    while hq:
        cnt, S, T = heapq.heappop(hq)

        # A 발차기
        if S + 1 == T:
            return cnt + 1
        # 더 커지는 경우는 제외
        elif S + 1 > T:
            continue
        else:
            heapq.heappush(hq, (cnt + 1, S + 1, T))

        # B 발차기
        if S * 2 == T + 3:
            return cnt + 1
        # 더 커지는 경우는 제외
        elif S * 2 > T + 3:
            continue
        else:
            heapq.heappush(hq, (cnt + 1, S * 2, T + 3))


C = int(input())
for tc in range(1, C + 1):
    # 태균 점수 S, 상대 점수 T
    S, T = map(int, input().split())

    print(kick(S, T))


