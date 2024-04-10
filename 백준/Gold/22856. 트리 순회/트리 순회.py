import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 트리 순회 (22856)
 1. 유사 중위 순회
  - 순회의 시작은 트리의 루트(1번 노드)
  - 순회의 끝은 중외 순회할 때 마지막 노드
 2. 진행
  - 현재 위치한 노드의 왼쪽 자식 노드 존재하고 방문하지 않았다면 왼쪽 자식 노드 방문
  - 그러지 않을 시, 오른쪽 자식 노드도 똑같이
  - 그렇지 않을 시, 현재 노드가 끝이라면 유사 중위 순회 종료
  - 그러지 않을 시,
[입력]
 1. N: 노드의 개수
 2. a: 현재 노드, b: 왼쪽 자식 노드, c: 오른쪽 자식 노드(-1로 주어지는 경우 자식 노드 없음)
[출력]
 1. 유사 중위 순회를 하면서 이동한 총 횟수 출력
"""

"""
<풀이>
 1. 트리
"""
sys.setrecursionlimit(10**9)


# 중위 순회
def inorder(now):
    global last
    # 왼쪽 자식 노드 탐색
    if left_children[now]:
        inorder(left_children[now])
    # 현재 위치를 마지막 노드로 교체
    last = now
    # 오른쪽 자식 노드 탐색
    if right_children[now]:
        inorder(right_children[now])


# 유사 중위 순회
def similar_inorder(now):
    global cnt

    # 왼쪽 자식 노드 탐색
    if left_children[now]:
        cnt += 1
        # print(f'left: {left_children[now]}')
        similar_inorder(left_children[now])

    # 마지막 노드일시 종료
    if now == last:
        print(cnt)
        exit()

    # 오른쪽 자식 노드 탐색
    if right_children[now]:
        cnt += 1
        # print(f'right: {right_children[now]}')
        similar_inorder(right_children[now])

    # 자식 탐색 후 부모가 있다면 리턴
    if now in set_left or now in set_right:
        # print(f'return: {now}')
        cnt += 1


# 우측 이동(돌아올 필요가 없는 우측 이동을 다시 하여 중복 제거)
def right(now):
    global cnt
    # 우측 탐색
    if right_children[now]:
        cnt -= 1
        right(right_children[now])


N = int(input())
# 자식들 정보(인덱스가 부모 노드)
left_children = [0] * (N + 1)
right_children = [0] * (N + 1)
for _ in range(N):
    a, b, c = map(int, input().split())

    if b != -1:
        left_children[a] = b
    if c != -1:
        right_children[a] = c

set_left = set(left_children)
set_right = set(right_children)
# 이동횟수와 마지막 노드
cnt = 0
last = 0
# 중위순회로 마지막 노드 찾은 후 유사 중위 순회
inorder(1)
similar_inorder(1)
print(visited)