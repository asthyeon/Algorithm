import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
<문제>
# 절댓값 힙 (11286)
1. 연산 절차
 - x: 배열에 정수 추가
 - 0: 절댓값이 가장 작은 값 출력, 그 값을 배열에서 제거
 - 절댓값이 가장 작은 값이 여러개일 때, 가장 작은 수 출력)
 - 배열이 비어있는 경우 0 출력
<풀이>
1. 우선순위큐 이용 -> 원소 2개를 이용해서 절댓값으로 선정렬, 정수값으로 후정렬
"""
import heapq

N = int(input())
hq = []
for _ in range(N):
    x = int(input())
    
    # 정수 인큐
    if x != 0:
        heapq.heappush(hq, (abs(x), x))
    # 배열이 비어있는 경우 0 출력
    elif not hq:
        print(0)
    # 값 출력
    else:
        print(heapq.heappop(hq)[1])