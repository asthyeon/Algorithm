import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 행렬
 1. 0과 1로만 이루어진 행렬 A와 행렬 B
 2. 행렬 A를 B로 바꾸는데 필요한 연산의 횟수의 최솟값 구하기
 3. 행렬을 변환하는 연산
  - 어떤 3x3 크기의 부분 행렬에 있는 모든 원소를 뒤집는 것(0 -> 1, 1 -> 0)
[입력]
 1. N, M: 행렬 크기
 2. 둘째 줄 ~ N개의 줄: 행렬 A
 3. 그 다음 줄 ~ N개의 줄: 행렬 B
[출력]
 1. 문제의 정답 출력
 2. 만약 A를 B로 바꿀 수 없다면 -1 출력
"""

"""
<풀이>
 1. 큐에다 행렬을 넣고 매번 연산하기 -> 메모리 초과
 2. 세트를 통해서 중복 제거 -> 불필요
 3. 재귀로 풀어보기 -> 재귀 초과
 4. 뒤집기 or 뒤집지 않기만 존재하므로 시작 칸이 같으면 넘어가고 다르면 바꾸기
 5. 계속 바꿔봐도 다르면 결국 같지 않은 것
"""


# 행렬 변환 연산
def calculate(A, B, cnt):
    # 행렬 변환
    for x in range(N - 2):
        for y in range(M - 2):
            # 시작 칸이 다르다면 변환
            if A[x][y] != B[x][y]:
                cnt += 1
                A[x][y] = change[A[x][y]]
                A[x + 1][y] = change[A[x + 1][y]]
                A[x][y + 1] = change[A[x][y + 1]]
                A[x + 1][y + 1] = change[A[x + 1][y + 1]]
                A[x + 2][y] = change[A[x + 2][y]]
                A[x][y + 2] = change[A[x][y + 2]]
                A[x + 2][y + 1] = change[A[x + 2][y + 1]]
                A[x + 1][y + 2] = change[A[x + 1][y + 2]]
                A[x + 2][y + 2] = change[A[x + 2][y + 2]]

            # B와 비교
            if A == B:
                return cnt

    # 변환할 수 없으면 -1 출력
    return -1


# 세로 N, 가로 M
N, M = map(int, input().split())
# 행렬 A
A = list(list(map(int, input().rstrip())) for _ in range(N))
# 행렬 B
B = list(list(map(int, input().rstrip())) for _ in range(N))

# 변환하지 않아도 될 경우
if A == B:
    print(0)

# 변환하는 경우
else:
    # 변환용 딕셔너리
    change = {0: 1, 1: 0}

    print(calculate(A, B, 0))






