"""
[문제] 더 맵게
1. Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶어함
2. Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 섞음
 - 섞은 음식의 스코빌 = 가장 안매운 스코빌 + (두 번째로 안매운 스코빌 * 2)
3. 모든 음식의 스코빌 지수가 K 이상이 될 때까지 필요한 최소 섞는 횟수?

[풀이]
1. 우선순위 큐
"""
import heapq


def solution(scoville, K):
    answer = 0
    
    # 일단 다 넣기
    hq = []
    for food in scoville:
        heapq.heappush(hq, food)
    
    # 2개씩 빼서 비교해보기
    while True:
        not_spicy1 = heapq.heappop(hq)
        # 가장 안매운 음식의 지수가 K 이상일 때 섞기 종료
        if not_spicy1 >= K:
            break
        
        # 음식이 1개만 남았을 때 종료
        if not hq:
            answer = -1
            break
        
        # 음식 섞기 
        answer += 1
        not_spicy2 = heapq.heappop(hq)
        
        # 섞기
        mixing = not_spicy1 + (not_spicy2 * 2)
        heapq.heappush(hq, mixing)
    
    return answer