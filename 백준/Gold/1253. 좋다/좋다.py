import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 좋다 (1253)
 1. N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 '좋다'고 함
 2. N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력
 3. 수의 위치가 다르면 값이 같아도 다른 수
[입력]
 1. N: 수의 개수
 2. 두번째 줄: i번째 수를 나타내는 A
[출력]
 1. 좋은 수의 개수 출력
"""

"""
<풀이>
 1. 투 포인터
 2. 어떤 수가 다른 수 두개의 합 -> 자기자신은 포함 안됨
 3. 모든 자리 수에 대한 투 포인터를 실행 + 이분탐색
"""


# 투 포인터
def two_pointer(A):
    # 정답 수
    cnt = 0
    # 모든 자리 순회
    for target in range(N):
        start = 0
        end = N - 1

        # 이분탐색
        while start < end:
            number = A[start] + A[end]

            # 더한 값이 이번 값과 같다면
            if number == A[target]:
                # 시작 값이 자기 자신이라면 증가
                if start == target:
                    start += 1
                # 끝 값이 자기 자신이라면 감소
                elif end == target:
                    end -= 1
                # 두 수가 자기 자신이 아니라면 정답 증가
                else:
                    cnt += 1
                    break

            # 더한 값이 이번 값보다 작다면 증가
            elif number < A[target]:
                start += 1

            # 더한 값이 이번 값보다 크다면 감소
            else:
                end -= 1

    return cnt


N = int(input())
A = list(map(int, input().split()))
A.sort()

print(two_pointer(A))