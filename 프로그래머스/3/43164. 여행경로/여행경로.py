"""
# 여행경로
 1. 주어진 항공권을 모두 이용하여 여행경로 짜기
 2. 항상 "ICN" 공항에서 출발
[입력]
 1. tickets: 항공권 정보가 담긴 2차원 배열
  - [출발지, 도착지]
[출력]
 1. 방문하는 공항 경로를 배열에 담아 출력
 2. 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로 출력
 3. 모든 도시를 방문할 수 없는 경우 X
"""

"""
<풀이>
 1. 백트래킹 이용하기
"""


def solution(tickets):
    # 여행경로들
    answer = []


    # 백트래킹
    def back_tracking(route, now, used):
        nonlocal answer
        if len(used) == len(tickets):
            answer.append(route)
            return

        for ticket in range(len(tickets)):
            if ticket in used:
                continue
            if now == tickets[ticket][0]:
                back_tracking(route + [tickets[ticket][1]], tickets[ticket][1], used + [ticket])

                
    back_tracking(['ICN'], 'ICN', [])
    return min(answer)