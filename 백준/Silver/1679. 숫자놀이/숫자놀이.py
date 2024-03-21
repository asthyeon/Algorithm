import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 숫자놀이(1679)
 1. 홀순이(holsoon)와 짝순이(jjaksoon)가 번갈아가며 서로 큰 수(1부터 1씩 증가) 만들기
  - 모든 숫자의 사용 횟수를 최대 K번까지 사용 가능
 2. 사용하는 정수에는 반드시 1이 포함됨
[입력]
 1. N: 사용되는 정수의 수
 2. 사용하는 정수가 크기 순으로 주어짐
 3. K: 최대 사용 횟수
[출력]
 1. 누가 몇 번째 수에서 이겼는지 출력
"""

"""
<풀이>
 1. 일단 풀어보기 -> 시간초과
 2. 시작 값을 갱신해보기 -> 시간초과 or 메모리 초과
- 1: [1]
- 2: [1 + 1]
- 3: [1 + 1 + 1] or [3]
- 4: [1 + 1 + 1 + 1] or [1 + 3]
- 5: [1 + 1 + 1 + 1 + 1] or [1 + 1 + 3]
- 6: [1 + 1 + 1 + 3] or [3 + 3]
- 7: [1 + 1 + 1 + 1 + 3] or [1 + 3 + 3]
- 8: [1 + 1 + 3 + 3]
- 9: [1 + 1 + 1 + 3 + 3] or [3 + 3 + 3]
- 10: [1 + 3 + 3 + 3]
- 11: [1 + 1 + 3 + 3 + 3]
- 12: [3 + 3 + 3 + 3]
- 13: [1 + 3 + 3 + 3 + 3]
- 14: X
 3. dp로 풀기
"""


# 각 인덱스에 해당하는 숫자를 몇개의 숫자로 만들 수 있는지 값 설정하는 dp
def dynamic_programming(numbers, K):
    INF = 10e9
    # 가능한 모든 숫자의 합과 마지막 조합이 안되는 수까지 만들기
    dp = [INF] * (numbers[-1] * K + 2)
    # 중복 처리용 세트
    set_numbers = set(numbers)

    for number in range(1, len(dp)):
        # 1개로 만들 수 있는 경우
        if number in set_numbers:
            dp[number] = 1
        # 여러 개의 숫자를 사용해야 하는 경우
        else:
            # 가능한 조합의 수 구하기
            for start in range(1, number + 1):
                dp[number] = min(dp[number], dp[start] + dp[number - start])

            # 승자 정하기
            if dp[number] > K:
                if number % 2 == 0:
                    winner = 'holsoon'
                else:
                    winner = 'jjaksoon'
                return f'{winner} win at {number}'


# 사용되는 정수의 수 N
N = int(input())
# 사용하는 정수들
numbers = list(map(int, input().split()))
# 최대 사용 횟수 K
K = int(input())

print(dynamic_programming(numbers, K))