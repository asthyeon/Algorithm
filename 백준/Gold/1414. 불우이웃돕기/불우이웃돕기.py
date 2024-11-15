import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 불우이웃돕기 (1414)
 1. N개의 방 각각에 모두 한 개의 컴퓨터가 존재하고 각각의 컴퓨터는 랜선으로 연결되어 있음
 2. 컴퓨터 A와 B가 있을 때,
  - 서로 랜선으로 연결되어 있으면 통신 가능
  - 또 다른 컴퓨터를 통해서 연결되어 있으면 통신 가능
[입력]
 1. N: 컴퓨터의 개수
 2. N개의 줄: 랜선의 길이
  - i번째 줄의 j번째 문자가 0인 경우: 컴퓨터 i와 j를 연결하는 랜선이 없음
  - a부터 z는 1부터 26, A부터 Z는 27부터 52
[출력]
 1. 다솜이가 기부할 수 있는 랜선의 길이의 최댓값 출력
   (만약 모든 컴퓨터가 연결되어 있지 않으면 -1 출력)
"""

"""
<풀이>
 1. MST
 2. 자기 자신 제외 및 최단 경로만 연결, 양방향
"""
import heapq

# 알파벳 치환
changer = {
    '0': 0,
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19,
    't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
    'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35,
    'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44,
    'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52,
}


def prim(computers):
    # 방문 리스트 및 우선순위큐
    visited = [0] * N
    hq = [(0, 0)]
    # 필요한 랜선 길이
    need = 0

    while hq:
        now_dist, now = heapq.heappop(hq)

        # 현재 노드 방문 처리
        if not visited[now]:
            visited[now] = 1
            need += now_dist

            for new_dist, new in computers[now]:
                # 컴퓨터 간 랜선이 있고, 방문하지 않은 노드라면
                if new_dist != 0 and not visited[new]:
                    # 방문 처리 및 인큐, 필요한 랜선 길이 추가
                    heapq.heappush(hq, (new_dist, new))

    # 방문하지 않은 노드가 없다면 (전체 합 - 필요한 랜선 길이) 출력
    if 0 not in visited:
        return total - need
    # 방문하지 않은 노드가 있다면 -1 출력
    else:
        return -1


N = int(input())
computers = [[] for _ in range(N)]
# 전체합 구하기
total = 0
for i in range(N):
    cable = input().rstrip()
    # 랜선 연결
    for j in range(N):
        # 변환된 값
        changed = changer[cable[j]]
        computers[i].append((changed, j))
        computers[j].append((changed, i))
        # 전체합도 동시에 구하기
        total += changed

print(prim(computers))