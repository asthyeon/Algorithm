import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 팀배분 (1953)
 1. 사람들이 각각 싫어하는 사람들의 정보가 주어짐
 2. 서로 싫어하는 사람은 같은 팀에 넣지 않으려 함
 3. n명의 사람들을 두 팀으로 나누기
[입력]
 1. n: 학생들의 수
 2. n개의 줄: 서로가 싫어하는 사람들의 정보(i번째 사람이 싫어하는 사람의 수와 사람들)
[출력]
 1. 청팀의 사람의 수 출력 
 2. 청팀에 속한 사람들을 오름차순 출력
 3. 백팀의 사람의 수 출력
 4. 백팀에 속한 사람들을 오름차순 출력(답이 여러 가지 일 경우에는 한 가지만 출력)
"""

"""
<풀이>
 1. 이분 그래프
"""
from collections import deque


def bfs(haters):
    visited = [0] * (n + 1)

    # 방문하지 않은 경우에만 출발
    for start in range(1, n + 1):
        if not visited[start]:
            q = deque([start])
            visited[start] = 1

            while q:
                now = q.popleft()

                for new in haters[now]:
                    if not visited[new]:

                        # 반대 숫자로 체크
                        if visited[now] == 1:
                            visited[new] = 2
                        else:
                            visited[new] = 1

                        q.append(new)

    # 팀 배분하기
    blue = []
    white = []

    for team in range(1, n + 1):
        if visited[team] == 1:
            blue.append(team)
        else:
            white.append(team)

    # 조건에 맞게 출력
    print(len(blue))
    print(*blue)
    print(len(white))
    print(*white)


n = int(input())
# 싫어하는 사람들
haters = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    hates = list(map(int, input().split()))

    # 싫어하는 사람 엮기(양방향시 중복됨)
    for j in range(1, hates[0] + 1):
        haters[i].append(hates[j])

bfs(haters)