"""
[문제] 이중우선순위큐
1. 연산규칙
 - I 숫자: 큐에 주어진 숫자 삽입
 - D 1: 큐에서 최댓값 삭제
 - D -1: 큐에서 최솟값 삭제
2. 모든 연산을 처리한 후 큐가 비어있으면 [0, 0], 비어있지 않으면 [최댓값, 최솟값] return
3. 최댓값/최솟값이 둘 이상인 경우, 하나만 삭제
4. 빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 해당 연산은 무시

[풀이]
1. 우선순위 큐
2. 이중으로 최솟값 큐, 최댓값 큐 이용
"""
import heapq


def solution(operations):
    answer = []
    
    hq_min = []
    hq_max = []
    # 연산 수행
    for operation in operations:
        command, number = map(str, operation.split())
        
        # 입력(최댓값은 부호 반대로)
        if command == 'I':
            heapq.heappush(hq_min, int(number))
            heapq.heappush(hq_max, -int(number))
        # 제거
        else:
            # 큐가 비어있지 않는 경우에만 수행
            if hq_min and hq_max:
                # 최댓값 삭제
                if number == '1':
                    maximum = -heapq.heappop(hq_max)
                    hq_min.remove(maximum)
                # 최솟값 삭제
                else:
                    minimum = -heapq.heappop(hq_min)
                    hq_max.remove(minimum)
    
    # 큐가 비어있을 때
    if not hq_min and not hq_max:
        answer.append(0)
        answer.append(0)
    # 큐가 비어있지 않다면
    else:
        answer.append(-heapq.heappop(hq_max))
        answer.append(heapq.heappop(hq_min))
        
    return answer