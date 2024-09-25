import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 용액 합성하기 (14921)
 1. 같은 양의 두 용액을 혼합하면 그 특성값은 두 용액의 특성값의 합이 됨
[입력]
 1. N: 용액 수
 2. A: 용액들의 특성값 리스트(오름차순으로 주어짐)
[출력]
 1. 두 개의 용액을 혼합하여 만들 수 있는 0에 가장 가까운 특성값 B 출력
"""

"""
<풀이>
 1. 투 포인터
"""

N = int(input())
A = list(map(int, input().split()))

start = 0
end = N - 1
# 0과의 차이
difference = A[start] + A[end]

while start < end:
    A_sum = A[start] + A[end]
    # 0과의 차이 갱신
    if abs(A_sum) < abs(difference):
        difference = A_sum
    # 0일 경우 종료
    if A_sum == 0:
        print(0)
        exit()
    # 0보다 작을 경우
    elif A_sum < 0:
        start += 1
    # 0보다 클 경우
    else:
        end -= 1

print(difference)