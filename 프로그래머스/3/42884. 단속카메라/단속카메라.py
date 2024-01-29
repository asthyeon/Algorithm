"""
# 단속카메라
 1. 모든 차량이 한 번은 단속용 카메라를 만나도록 설치
 2. 차량 진입/진출 지점에 카메라가 설치되어 있어도 카메라를 만난 것
[입력]
 1. routes: [start, end]의 차량 이동 경로가 i개 주어짐
[출력]
 1. 최소 몇 대의 카메라를 설치해야 하는가?
"""

"""
<풀이>
 1. 진출로를 기준으로 생각하기
"""

def solution(routes):
    answer = 1
    
    # 진출로 기준 정렬
    routes.sort(key=lambda x: x[1])
    
    # 이전 진출로
    previous = routes[0][1]
    for route in range(1, len(routes)):
        # 이전 진출로보다 진입로 위치가 더 앞설 경우 진출로 교체 및 카메라 설치
        if previous < routes[route][0]:
            previous = routes[route][1]
            answer += 1

    return answer