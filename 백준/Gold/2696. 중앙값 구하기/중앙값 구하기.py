import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 중앙값 구하기 (2696)
 1. 우선순위큐 -> 최대힙, 최소힙 이용
 2. 최대힙 -> 최소힙 순서로 저장, 최대힙의 top은 최소힙의 top보다 작아야 함
 3. 최대힙의 top = 중앙값
"""
import heapq

# 테스트 케이스
T = int(input())
for tc in range(1, T + 1):
    # 수열의 길이, 수열
    M = int(input())
    sequences = []
    # 수열 입력 받기(extend 활용)
    for _ in range((M // 10) + 1):
        sequence = list(map(int, input().split()))
        sequences.extend(sequence)

    # 최대힙(중앙값 이내), 최소힙(중앙값 초과), 정답
    max_heap = []
    min_heap = []
    answer = []

    for i in range(M):
        # 홀수 번째일 때
        if i % 2 == 0:
            heapq.heappush(max_heap, (-sequences[i], sequences[i]))
            # 최소힙의 top과 비교
            if min_heap:
                if min_heap[0] < max_heap[0][1]:
                    min_top = heapq.heappop(min_heap)
                    max_top = heapq.heappop(max_heap)[1]
                    heapq.heappush(min_heap, max_top)
                    heapq.heappush(max_heap, (-min_top, min_top))
            answer.append(max_heap[0][1])
        # 짝수 번째일 때
        else:
            heapq.heappush(min_heap, sequences[i])
            # 최대힙의 top과 비교
            if min_heap[0] < max_heap[0][1]:
                min_top = heapq.heappop(min_heap)
                max_top = heapq.heappop(max_heap)[1]
                heapq.heappush(min_heap, max_top)
                heapq.heappush(max_heap, (-min_top, min_top))

    # 정답 출력
    length = (M // 2) + 1
    print(length)
    for j in range((length // 10) + 1):
        print(*answer[j * 10:(j + 1) * 10])


