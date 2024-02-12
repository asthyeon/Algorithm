import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 화살표 그리기(15970)
 1. 같은 색상의 점 서로 잇기(같은 색상인 다른 점이 항상 존재)
 2. 점 p에서 시작해 q로 가는 하나의 화살표를 항상 그릴 수 있음
 3. 가장 가까운 점만 그릴 수 있음
 4. 점들의 위치와 색상이 주어질 때 모든 점에서 시작하는 화살표들의 길이 합 찾기
[입력]
 1. N: 점들의 개수
 2. 점의 좌표(x: 좌표, y: 색상)
[출력]
 1. 모든 점에서 시작하는 화살표들의 길이 합 출력
"""

"""
<풀이>
 1. 일단 풀어보기
"""


# 화살표 길이 계산
def arrow(locations):
    # 총 길이
    answer = 0
    
    # 좌우 길이 비교
    for i in range(len(locations)):
        # 처음 예외 처리
        if i == 0:
            answer += locations[i + 1][1] - locations[i][1]
        # 마지막 예외 처리
        elif i == len(locations) - 1:
            answer += locations[i][1] - locations[i - 1][1]
        # 색상이 같다면 거리 계산, 같지 않다면 가장 큰 값으로 대체
        else:
            if locations[i - 1][0] == locations[i][0]:
                left = locations[i][1] - locations[i - 1][1]
            else:
                left = 10e9
            if locations[i + 1][0] == locations[i][0]:
                right = locations[i + 1][1] - locations[i][1]
            else:
                right = 10e9

            answer += min(left, right)

    return answer


# 점들의 개수 N
N = int(input())
# 점의 좌표들
locations = []
for _ in range(N):
    x, y = map(int, input().split())

    # 색상 먼저 집어넣기
    locations.append((y, x))

# 색상 순으로 정렬
locations.sort()

print(arrow(locations))