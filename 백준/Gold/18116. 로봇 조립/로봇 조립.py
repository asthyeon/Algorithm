import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 로봇 조립 (18116)
 1. 부품 i가 속한 로봇: robot(i)
 2. 서로 다른 로봇은 공통 부품을 가지지 않음
[입력]
 1. N: 호재의 지시 횟수
 2. 부품 2개가 같은 로봇의 부품인지 알려줄 때에는 I a b의 형태(a와 b는 같은 로봇의 부품)
 2. 어떤 로봇의 부품이 몇 개인지 물어볼 때에는 Q c의 형태(c의 부품이 몇개냐)
[출력]
 1. Q로 시작하는 입력에 대해서 한 줄에 하나씩, 지금까지 알아낸 해당 로봇의 부품 개수 출력
"""

"""
<풀이>
 1. 유니온 파인드
 2. 자식에 해당하는 노드의 부품 전체를 넣어야 함
"""


# 루트를 찾는 find 함수
def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


# 노드 a와 b의 루트 노드 설정
def union(a, b):
    a = find(a)
    b = find(b)

    # 각 루트 노드 설정 후 부품 수 추가
    if a < b:
        parents[b] = a
        robots[a] += robots[b]
    # 같은 경우는 추가 X
    elif a > b:
        parents[a] = b
        robots[b] += robots[a]


N = int(input())
# 각 로봇의 부품 수와 부모 노드
robots = [1] * (10 ** 6 + 1)
parents = [i for i in range(10 ** 6 + 1)]
for _ in range(N):
    command = list(map(str, input().split()))

    # 같은 부품인 것을 알려줄 때
    if command[0] == 'I':
        union(int(command[1]), int(command[2]))

    # 지금까지 알아낸 로봇 부품 개수 출력 -> find로 부모 노드를 찾아야 함
    else:
        print(robots[find(int(command[1]))])