import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 사촌 (9489)
 1. 증가하는 정수 수열을 이용해서 트리를 만드는 방법
  - 첫 번째 정수는 트리의 루트 노드
  - 다음에 등장하는 연속된 수의 집합은 루트의 자식을 나타냄
  - 이 집합에 포함되는 수의 첫 번째 수는 루트 노드+1 보다 큼
  - 그 다음부터는 모든 연속된 수의 집합은 아직 자식이 없는 노드의 자식이 됨
  - 그러한 노드가 여러 가지 인 경우에는 가장 작은 수를 가지는 노드의 자식이 됨
  - 집합은 수가 연속하지 않는 곳에서 구분됨
 2. 두 노드의 부모는 다르지만, 두 부모가 형제일 때 두 노드를 사촌이라고 함
[입력]
 1. 여러 개의 테스트 케이스
 2. n: 노드의 수, k: 사촌의 수를 구해야 하는 노드의 번호
 3. n개: 증가하는 수열
 4. 입력의 마지막 줄에는 0이 두 개 주어짐
[출력]
 1. 각 테스트 케이스마다 k의 사촌 수 출력
"""

"""
<풀이>
 1. 트리
 2. 할아버지를 찾고 손자들의 수가 곧 사촌의 수
 3. 형제는 제외하기
"""

while True:
    n, k = map(int, input().split())

    # 종료 조건
    if n == 0 and k == 0:
        break

    # 증가하는 수열
    sequence = list(map(int, input().split()))

    # 부모가 누구인가
    parents = [-1] * n
    parent = 0
    target_parent = 0

    # 루트 노드는 건너뛰고 순회
    for i in range(1, n):

        # 처음은 무조건 루트의 자식
        if i == 1:
            parents[i] = parent

        # 그 이후는
        else:
            # 이전 값과 1 차이가 나면 같은 부모
            if sequence[i - 1] + 1 == sequence[i]:
                parents[i] = parent
            # 차이가 더 크다면 부모 변경
            else:
                parent += 1
                parents[i] = parent

        # 타겟의 부모 찾기
        if sequence[i] == k:
            target_parent = parent

    # 타겟의 조부모 찾기
    target_grandparent = parents[target_parent]

    # 사촌 수 세기
    cousin = 0
    for j in range(1, n):

        # 부모는 같지 않고(형제 X), 조부모가 같은 경우엔 사촌
        if parents[j] != target_parent and parents[parents[j]] == target_grandparent:
            cousin += 1

    print(cousin)













