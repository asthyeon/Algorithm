import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 단절점과 단절선(14675)
 1. 단절점: 해당 정점을 제거했을 때, 그 정점이 포함된 그래프가 2개 이상으로 나뉘는 경우
 2. 단절선: 해당 간선을 제거했을 때, 그 간선이 포함된 그래프가 2개 이상으로 나뉘는 경우
 3. 트리: 사이클이 존재하지 않으며 모든 정점이 연결되어 있는 그래프
[입력] 
 1. N: 트리의 정점 수
 2. N - 1개의 줄: 간선의 정보 a정점과 b정점은 연결되어 있다
 3. q: 질의의 수
 4. q줄: t가 1일 때는 k번 정점이 단절점인지에 대한 질의, 2일 때는 k번 간선이 단절선인지
[출력]
 1. 질의가 맞다면 'yes', 틀리면 'no'
"""

"""
<풀이>
 1. 트리
 2. 단절점 -> 연결된 정점이 1개일 때
 3. 단절선 -> 모든 선이 단절선
"""

# 정점 수 N
N = int(input())
# 트리 정보
tree = [[] for _ in range(N + 1)]
# 간선 정보
for _ in range(N - 1):
    # a정점과 b정점 양방향 연결
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# 질의의 수 q
q = int(input())
# 질의 정보
for _ in range(q):
    # 명령 정보 t, 확인해야 하는 번호 k
    t, k = map(int, input().split())

    # 단절점 파악
    if t == 1:
        # 연결 선이 1개일 때 단절점 X
        if len(tree[k]) == 1:
            print('no')
        else:
            print('yes')
    # 단절선 파악
    elif t == 2:
        print('yes')