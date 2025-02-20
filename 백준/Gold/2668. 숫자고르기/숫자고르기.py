import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 숫자고르기 (2668)
 1. 첫째 줄은 1 ~ N이 차례대로 있음
 2. 둘째 줄은 랜덤하게 들어가 있음
 3. 뽑은 정수들이 첫째 줄과 둘째 줄의 정수가 같도록
[입력]
 1. N: 칸의 길이
 2. N개의 줄: 들어가는 정수들이 하나씩
[출력]
 1. 뽑힌 정수들의 개수 출력, 그 다음 줄부터는 작은 수부터 큰 수의 순서로 한 줄에 하나씩 출력 
"""

"""
<풀이>
 1. dfs -> 사이클
"""


def dfs(start):
    visited[start] = 1
    # 다음 위치 확인
    for new in graph[start]:
        # 방문하지 않았다면 방문 처리
        if not visited[new]:
            dfs(new)
        # 방문한 곳이고, 사이클이 파악된다면 정답 추가
        elif visited[new] and new in graph[start]:
            answer.append(new)


N = int(input())
# 그래프 형성
graph = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    number = int(input())
    graph[number].append(i)

answer = []
# 각 번호에서 순회하여 사이클 파악
for start in range(1, N + 1):
    visited = [0] * (N + 1)
    dfs(start)

# 정렬
answer.sort()
print(len(answer))
for a in answer:
    print(a)