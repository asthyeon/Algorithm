import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 카드 정렬하기(1715)
 1. 정렬된 두 묶음의 숫자 카드
 2. 각 묶음의 카드 수를 A, B라 하면 보통 두 묶음을 합쳐서 하나로 만드는 데 A + B 번 비교
[입력]
 1. N: 숫자 카드 묶음 수
 2. N개의 줄: 숫자 카드 묶음
[출력]
 1. 최소 비교 횟수 출력
"""

"""
<풀이>
 1. 가장 짧은 것 끼리 합쳐보기 -> X
 2. 힙큐로 그 순간에 가장 짧은 것을 합쳐야 함
"""
import heapq


# 비교하기
def compare(cards, N):
    answer = 0

    # 비교를 안하는 경우
    if N == 0:
        return answer

    # 비교하는 경우
    while cards:
        # 현재 가장 작은 카드 꺼내기
        A = heapq.heappop(cards)
        if cards:
            B = heapq.heappop(cards)
        else:
            break

        # 합쳐서 더하기
        mix = A + B
        # 비교 횟수 추가
        answer += mix
        # 새로운 카드 생성
        heapq.heappush(cards, mix)

    return answer


# 카드 묶음 수 N
N = int(input())
# 카드 정보 입력
cards = []
for _ in range(N):
    card = int(input())
    cards.append(card)
cards.sort()

print(compare(cards, N))