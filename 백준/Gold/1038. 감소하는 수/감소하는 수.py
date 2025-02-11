import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 감소하는 수 (1038)
 1. 음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면,
 2. 그 수를 감소하는 수
[입력]
 1. N: 수
[출력]
 1. N번째 감소하는 수를 출력(없다면 -1 출력)
"""

"""
<풀이>
 1. 조합
"""
from itertools import combinations

N = int(input())

# 감소하는 모든 수의 조합 만들기
numbers = []
# 1자리부터 10자리
for i in range(1, 11):
    # 자리마다 모든 수를 조합
    for combi in combinations([i for i in range(10)], i):
        # 수를 만들고 역순으로 리스트에 넣기
        number = "".join(map(str, combi))
        numbers.append(int(number[::-1]))

# 감소하는 수가 있는 경우
if len(numbers) > N:
    # 정렬 후 출력
    numbers.sort()
    print(numbers[N])
# 감소하는 수가 없는 경우
else:
    print(-1)