import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 교차개수세기
1. 각각 N개의 쌍으로 이루어진 2N개의 정점과 M개의 간선으로 구성된 이분 그래프가 주어질 때
2. 서로 교차하는 총 개수 구하기
 - 교차조건: 독립 집합 A와 독릭 집합 B가 연결된 두 개의 간선을 (A1, B1), (A2, B2)라고 할 때,
             A1 < A2, B1 > B2 or A1 > A2, B1 < B2를 만족한다면 두 간선을 교차한다고 함
* 입력
- 첫 줄에 N과 간선의 개수 M
- 그 다음 줄부터 M+1번째 줄까지 두 개의 수(i, j)가 주어짐
 (이는 왼쪽 그룹의 i번 정점과 오른쪽 그룹의 j번 정점을 연결하는 간선이 있다는 의미
- 중복되는 간선이 주어지지는 않음
[출력: 주어진 간선이 교차하는 총 개수를 출력]
"""

"""
@ 풀이
(1) 세그먼트 트리 이용
(2) inversion counting 이용(펜윅트리)
 - n + 1의 크기를 가진 tree 배열을 만들고 tree[x]는 [1, x]까지 연결된 선분의 수를 나타냄
 - edges[index]는 index가 연결된 위치
 - index를 인덱스로 반복문을 돌리면서 edges[index] 값을 통해 답을 도출해낼 수 있음
 - 예: 이미 연결된 선의 개수 - 자신과 겹치지 않는 선 개수 구하기
      (index - edges[index])
 - i, j가 있을 때 i를 오름차순으로 정렬하고 j에 대해서 자신보다 앞에 선이 몇 개있는지 카운트
(3) 펜윅트리
 - 세그먼트 트리에서 각 층에서 짝수 인덱스를 무시하고 위로 올라가는 트리
 - 가장 밑에부터 올라가기 때문에 부모노드의 인덱스가 더 값이 큼
"""


# 트리 값 수정 함수
def modify(connection):
    # 인덱스가 트리 크기보다 작거나 같다면
    while connection <= N:
        # 트리의 인덱스 값에 1을 더하기(선을 하나 연결함)
        tree[connection] += 1
        # 비트 연산으로 현재 인덱스에서 자식 노드로 이동하는 과정
        connection += connection & -connection


# 해당 노드가 교차하는 간선 개수 구하기
def prefix_sum(connection):
    # 교차하는 간선 수
    cnt = 0
    # 해당 노드가 0보다 크다면
    while connection > 0:
        # 해당 노드에 교차하는 간선 수 더하기
        cnt += tree[connection]
        # 비트연산으로 펜윅트리에서 현재 인덱스에서 부모 노드로 이동하는 과정
        connection -= connection & -connection
    return cnt


# 쌍의 수 N, 간선의 수 M
N, M = map(int, input().split())
# 간선 정보 입력
edges = []
for _ in range(M):
    # i번 정점과 j번 정점
    i, j = map(int, input().split())

    # 간선 정보 저장
    edges.append((i, j))

# 간선 역방향 정렬
edges.sort(reverse=True)

# 트리 생성
tree = [0] * 2009

# 전체 교차하는 선 개수
total = 0
# 정렬된 간선 순회
for edge in range(M):
        # 전체 교차하는 선 개수에 현재 인덱스와 해당하는 노드까지의 누적 합의 차이를 더하기
        total += prefix_sum(edges[edge][1])
        # 연결된 노드 값 수정(교차하는 선 개수 추가)
        modify(edges[edge][1] + 1)

print(total)