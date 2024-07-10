import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 끝나지 않는 파티 (11265)
 1. 단방향 도로를 이용하여 한 파티장에서 다른 파티장에까지 시간내에 도착할 수 있는지 없는지 알아보기
 2. 직접 연결이 된 도로보다 경유하는 경우 더 빠를 수 있음
[입력]
 1. N: 파티장의 크기, M: 서비스를 요청한 손님의 수
 2. N개의 줄: i번째 줄의 j번째 수 T: i번 -> j번으로 직접 연결된 도로를 통해 이동하는 시간
 3. 다음 M개의 줄: A: 서비스를 요청한 손님이 위치한 파티장, B: 다음 파티장, C: 다음 파티까지의 시간
[출력]
 1. 서비스를 요청한 손님이 시간 내에 도착할 수 있으면 "Enjoy other party", 아니면 "Stay here" 출력
"""

"""
<풀이>
 1. 다익스트라 -> 보다는 플로이드-워셜로 한 번 구해놓고 값만 출력하기
"""


# 플로이드-워셜
def floyd_warshall(halls):
    # 경유 지점
    for transit in range(1, N + 1):
        # 시작점
        for start in range(1, N + 1):
            # 도착점
            for end in range(1, N + 1):
                # 자기 자신인 경우 0으로 갱신
                if start == end:
                    halls[start][end] = 0
                # 바로 가는 경유와 경유하는 경유 중 더 빠른 값으로 값 갱신
                halls[start][end] = min(halls[start][end], halls[start][transit] + halls[transit][end])


N, M = map(int, input().split())
# 파티장 -> 각 파티장별 최단 거리를 담을 배열
halls = [[10e9] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    roads = [0] + list(map(int, input().split()))

    # 길 연결
    for j in range(1, N + 1):
        # 자기 자신일 때는 생략
        if not roads[j]:
            continue
        halls[i][j] = roads[j]

# 최단 거리 갱신
floyd_warshall(halls)

# 손님들의 요청
for _ in range(M):
    A, B, C = map(int, input().split())

    # 제 시간에 도달할 수 있다면 파티 즐기기
    if halls[A][B] <= C:
        print("Enjoy other party")
    # 그렇지 않으면 머물러라
    else:
        print("Stay here")