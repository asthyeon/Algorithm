import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 수들의 합 4(2015)
 1. 배열 A: A[1], A[2], ..., A[N]
 2. 배열 A의 부분 집합: A[i]부터 A[j]까지의 합
 3. N x (N + 1) / 2 개의 부분합 중 합이 K인 것이 몇 개나 있는지?
[입력]
 1. N, K: 배열 A의 길이 N, 조건 값 K
 2. 배열 A
[출력]
 1. 합이 K인 부분합의 개수 출력
"""

"""
<풀이>
 1. 일단 풀어보기
 2. 누적합 단순 이중포문 -> 시간초과
 3. 누적합에 딕셔너리로 각 누적합이 나온거를 딕셔너리에 기록하기
"""

# 배열 A의 길이 N, 합 조건 값 K
N, K = map(int, input().split())
# 배열 A
A = list(map(int, input().split()))

# 누적합 딕셔너리
prefix_dict = {}
# 누적합
prefix_sum = 0
# 누적합 수
cnt = 0

prefix_dict[0] = 1
for i in range(N):
    # 누적
    prefix_sum += A[i]

    # 이전까지의 누적 합 중에 K 차이만큼 나면 값이 K 인 부분집합이 있는 것
    if prefix_sum - K in prefix_dict:
        cnt += prefix_dict[prefix_sum - K]

    # 딕셔너리에 있으면 + 1, 없으면 0 + 1
    prefix_dict[prefix_sum] = prefix_dict.get(prefix_sum, 0) + 1

print(cnt)



