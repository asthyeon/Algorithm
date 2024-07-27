import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 대표 자연수 (2548)
 1. 대표 자연수: 주어진 모든 자연수들에 대하여 그 차이를 계산하여 그 차이들 전체의 합을 최소로
[입력]
 1. N: 자연수 개수
 2. 수 리스트
[출력]
 1. 대표 자연수 출력 (2개 이상일 경우 그 중 제일 작은 것 출력)
"""

"""
<풀이>
 1. 일단 풀어보기
"""


# 차이 합 구하기
def calculator(number):
    total = 0

    # 합 계산
    for other in numbers:
        if number != other:
            total += abs(number - other)

    return total


N = int(input())
numbers = list(map(int, input().split()))

# 수 차이의 합에 대한 딕셔너리
differences = {}
# 수 차이 계산
for number in numbers:
    # 합 구하기
    differ = calculator(number)
    # 이번 합이 없다면
    if differ not in differences:
        # 합을 key로, 그에 해당하는 자연수를 value로
        differences[differ] = number
    # 이번 합이 있다면
    else:
        # 더 작은 자연수로 교체
        differences[differ] = min(number, differences[differ])

# 대표 자연수 출력
print(differences[min(differences)])