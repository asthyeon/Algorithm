import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 카드 정렬하기 (1715)
1. 각 묶음의 카드 수를 A, B라 할 때,
2. 두 묶음을 합쳐서 하나로 만드는 데에는 A+B번의 비교를 해야 함
3. 최소 횟수로 비교하기

[풀이]
1. 우선순위 큐
2. 가장 작은 값부터 합치기
"""
import heapq

N = int(input())
hq = []
for _ in range(N):
    card = int(input())
    heapq.heappush(hq, card)

cnt = 0
while hq:
    A = heapq.heappop(hq)
    # 배열이 비어있지 않다면
    if hq:
        B = heapq.heappop(hq)
    # 배열이 비어있다면 종료
    else:
        break

    # 비교값 더하기, 비교한 값을 다시 인큐
    cnt += (A + B)
    heapq.heappush(hq, A + B)

print(cnt)
