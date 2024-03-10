import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 회사 문화 1(14267)
 1. 내리칭찬
  - 상사가 한 직속 부하 칭찬시 그 부하의 모든 부하들이 칭찬 받음
 2. 모든 칭찬에는 칭찬의 정도를 의미하는 수치가 있는데 이 수치 또한 똑같이 칭찬 받음
[입력]
 1. n: 직원 수, m: 칭찬 수
 2. 직원 n명의 직속 상사 번호 주어짐(상사 번호가 더 작음, 사장은 1번, 사장 상사는 없으므로 -1)
 3. m줄: 칭찬 정보
 4. 사장은 상사가 없으므로 칭찬 X
[출력]
 1. 1번부터 n번의 직원까지 칭찬을 받은 정도 출력
"""

"""
<풀이>
 1. 일단 풀어보기
"""
from collections import deque


# 직원 수 n, 칭찬 수 m
n, m = map(int, input().split())
# 직속 상사 번호
parents = [0] + list(map(int, input().split()))
# 칭찬 정보
praises = deque([0] * (n + 1))
for _ in range(m):
    # 직속 상사로부터 칭찬을 받은 직원 번호 i, 칭찬의 수치 w
    i, w = map(int, input().split())
    # 칭찬 정보 더하기
    praises[i] += w

# 사장을 제외한 직원들의 직속 상사 칭찬 점수 더하기
for j in range(2, n + 1):
    praises[j] += praises[parents[j]]

# 맨 왼쪽을 제거하고 출력
praises.popleft()
print(*praises)