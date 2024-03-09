import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 민서의 응급 수술(20955)
 1. 뉴런을 하나의 트리 형태로 연결(사이클 X)
 2. 두 뉴런을 연결 or 두 뉴런 연결 해제 가능
 3. 두 뉴런 사이에는 최대 1개의 시냅스만 존재
[입력]
 1. N: 뉴런 수, M: 시냅스 수
 2. M개의 줄: 시냅스로 연결된 두 뉴런의 번호 u, v
[출력]
 1. 모든 뉴런을 트리 형태로 연결하기 위한 최소 연산 횟수
"""

"""
<풀이>
 1. 유니온 파인드
 2. 결국은 다 하나의 부모를 가져야함
"""


# find
def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


# union
def union(x, y, is_connected):
    x = find(x)
    y = find(y)

    # 사이클일시
    if parents[x] == parents[y]:
        return 1
    elif parents[x] > parents[y]:
        parents[x] = y
        # 이미 연결된 뉴런이라면 연산 X
        if is_connected:
            return 0
        # 연결되지 않은 뉴런일시 연산
        else:
            return 1
    else:
        parents[y] = x
        # 이미 연결된 뉴런이라면 연산 X
        if is_connected:
            return 0
        # 연결되지 않은 뉴런일시 연산
        else:
            return 1


# 뉴런 수 N, 시냅스 수 M
N, M = map(int, input().split())
parents = [i for i in range(N + 1)]
# 연산 수
cnt = 0
# 뉴런 정보
for _ in range(M):
    x, y = map(int, input().split())
    # 사이클일 경우 뉴런 연결 해제 연산(연산 수 + 1)
    cnt += union(x, y, True)

# 연결되지 않은 뉴런 연결
for child in range(2, N + 1):
    if find(1) != find(child):
        cnt += union(1, child, False)

print(cnt)