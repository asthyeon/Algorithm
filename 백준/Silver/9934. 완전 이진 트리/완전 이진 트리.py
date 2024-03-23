import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 완전 이진 트리(9934)
 1. 깊이가 K인 완전 이진트리는 총 2K-1개의 노드로 이루어져 있음
 2. 마지막 레벨을 제외한 모든 집은 왼쪽 자식과 오른쪽 자식을 가짐
 3. 어떤 순서로 도시를 방문했는지 기억
  (1) 처음은 트리의 루트
  (2) 현재 빌딩의 왼쪽 자식 빌딩 안들어갔다면 왼쪽 자식으로 이동
  (3) 현재 있는 노드가 왼쪽 자식이 없거나 왼쪽 자식에 있는 빌딩 들어간거라면 번호 적기
  (4) 현재 빌딩을 이미 들어갔다 나왔고, 오른쪽 자식을 가지고 있는 경우라면 오른쪽 자식 이동
  (5) 현재 빌딩과 왼쪽, 오른쪽 자식 모두 방문시 부모 노드 이동
[입력]
 1. K: 트리의 깊이
 2. 상근이가 방문한 빌딩의 번호가 순서대로 주어짐
[출력]
 1. 각 레벨에 있는 빌딩의 번호 구하기
"""

"""
<풀이>
 1. 중위 순회: 왼쪽 -> 루트 -> 오른쪽
"""


# 트리 방문
def visit_tree(record, now):
    # 현재 레벨에 해당 하는 루트 노드
    root = len(record) // 2
    # 트리에 루트 노드 추가
    tree[now].append(record[root])
    # 마지막 레벨에 방문한 경우 돌아가기
    if len(record) == 1:
        return
    # 왼쪽 자식 탐색
    visit_tree(record[:root], now + 1)
    # 오른쪽 자식 탐색
    visit_tree(record[root + 1:], now + 1)


# 트리의 깊이 K
K = int(input())
# 방문 기록
record = list(map(int, input().split()))
# 트리
tree = [[] for _ in range(K)]
# 루트 노드를 찾아서 탐색 시작
visit_tree(record, 0)

for k in range(K):
    print(*tree[k])