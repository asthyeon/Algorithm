import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 가장 가까운 세 사람의 심리적 거리 (20529)
 1. 세 사람의 심리적 거리 구하기
 2. 두 사람 사이의 유형이 다르면 심리적인 거리 +
 3. 세 사람의 심리적인 거리 = AB 거리 + BC 거리 + CA 거리
[입력]
 1. T: 테스트 케이스 수
 2. N: 학생의 수
 3. 두번째 줄: 각 학생의 MBTI
[출력]
 1. 가장 가까운 세 학생 사이의 심리적인 거리 구하기
"""

"""
<풀이> 
 1. 이미 푼 문제
 2. 비둘기집 원리
  - 비둘기가 n마리, 비둘기 집이 m개 있을 때,
  - n이 m보다 크면 적어도 하나의 집에는 비둘기가 2마리 이상 들어간다는 원리
  - 16 x 2 + 1이 될 경우 적어도 3명은 겹치게 됨 -> 심리적 거리 0
"""


# 세 사람 사이의 거리 구하기
def distant(A, B ,C):
    dist = 0
    for i in range(4):
        # 세 명과 비교
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

    mbti = list(map(str, input().split()))

    # 학생 수가 32 초과일 경우 -> 적어도 3명은 겹쳐짐 = 심리적 거리 0
    if N > 32:
        print(0)

    else:
        # 세 사람의 심리적 거리 최대 값 = 12 (AB = 4, BC = 4, CA = 4)
        answer = 12

        # 순회
        for A in range(N - 2):
            for B in range(A + 1, N - 1):
                for C in range(B + 1, N):
                    answer = min(answer, distant(mbti[A], mbti[B], mbti[C]))

        print(answer)
