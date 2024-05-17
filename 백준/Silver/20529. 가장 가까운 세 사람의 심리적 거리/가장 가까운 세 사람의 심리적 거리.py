import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 가장 가까운 세 사람의 심리적 거리 (20529)
 1. MBTI에서 다른 알파벳 하나당 심리적 거리 +1
 2. 세 사람의 심리적 거리
  = (A & B) + (B & C) + (C & A)
[입력]
 1. T: 테스트 케이스 수
 2. N: 학생의 수
[출력]
 1. 각 테스트 케이스에 대한 답을 한 줄에 하나씩 출력
"""

"""
<풀이>
 1. 비둘기집 원리
  - 비둘기가 n마리, 비둘기 집이 m개 있을 때,
  - n이 m보다 크면 적어도 하나의 집에는 비둘기가 2마리 이상 들어간다는 원리
  - 16 x 3이 될 경우 적어도 3명은 겹치게 됨 -> 심리적 거리 0
"""


# 심리적 거리 구하기
def cal(A, B, C):
    dist = 0
    for i in range(4):
        if A[i] != B[i]:
            dist += 1
        if B[i] != C[i]:
            dist += 1
        if C[i] != A[i]:
            dist += 1

    return dist


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    students = list(map(str, input().split()))

    # 비둘기집 원리
    if N > 32:
        print(0)

    else:
        # 최댓값
        answer = 12

        # 세 수 순회
        for A in range(N):
            for B in range(A + 1, N):
                for C in range(B + 1, N):
                    answer = min(answer, cal(students[A], students[B], students[C]))

        print(answer)


