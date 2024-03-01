"""
# 입국심사
 1. 한 심사대에서는 동시에 한 명만 심사 가능
 2. 가장 앞에 서 있는 사람은 비어 있는 심사대로 가서 심사 받기 가능
 3. 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로 가서 심사 받기 가능
[입력]
 1. n: 입국심사를 기다리는 사람 수
 2. times: 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열
[출력]
 1. 모든 사람이 심사를 받는데 걸리는 시간의 최솟값 출력
"""

"""
<풀이>
 1. 이분탐색 이용
 2. 시간의 값을 이분탐색
"""

def solution(n, times):
    answer = 0
    
    # 이분탐색
    start = 1
    end = 1000000000 * n

    while start <= end:
        middle = (start + end) // 2
        passed = 0

        # 한 심사대에서 통과한 사람 구하기
        for time in times:
            passed += middle // time

        # 통과한 사람이 n명보다 같거나 많다면 시간 최적화하기
        if passed >= n:
            end = middle - 1
            # n명보다 같거나 많기 때문에 답 배정
            answer = middle
        
        # 통과한 사람이 더 적다면 시간 늘리기
        else:
            start = middle + 1
            
    return answer