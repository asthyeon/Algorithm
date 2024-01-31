import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 금민수의 개수
 1. 은민이는 4, 7 좋아함
 2. 금민수: 어떤 수가 4와 7로만 이루어짐
[입력]
 1. 1 <= A <= B <= 1000000000
[출력]
 1. B >= (어떤 수) >= A 를 만족하는 금민수 개수 출력
"""

"""
<풀이>
 1. 중복 순열 이용
 2. A보다 크거나 같은 값부터 B보다 작거나 같은 값까지만 구하기
"""
from itertools import product


# 금민수 시작점 찾기
def count_start_minsu(A, minsus):
    # 각 순열 값을 숫자로 만들고 비교
    for minsu in range(len(minsus)):
        gold = ''
        for m in minsus[minsu]:
            gold += m

        # A보다 크거나 같은 값을 찾으면 A부터의 길이를 넣기
        if A <= int(gold):
            return len(minsus[minsu:])

    # 시작점을 못찾으면 0 반환
    return 0


# 금민수의 시작점과 끝점이 같은 자리 수일 때
def count_same_minsu(A, B, minsus):
    # 시작점 찾기
    start = -1
    # 각 순열 값을 숫자로 만들고 비교
    for minsu in range(len(minsus)):
        gold = ''
        for m in minsus[minsu]:
            gold += m

        # A보다 크거나 같은 값을 찾으면 A부터의 길이를 넣기
        if A <= int(gold):
            start = minsu
            break

    # 끝점 찾기
    end = -1
    # 각 순열 값을 숫자로 만들고 비교
    for minsu in range(len(minsus) - 1, -1, -1):
        gold = ''
        for m in minsus[minsu]:
            gold += m

        # B보다 작거나 같은 값을 찾으면 거기까지의 길이를 넣기
        if B >= int(gold):
            end = minsu
            break

    if start == -1 or end == -1:
        return 0
    else:
        return len(minsus[start:end + 1])


# 금민수 끝점 찾기
def count_end_minsu(B, minsus):
    # 자리 수가 B보다 작다면 그대로 다 넣기
    if len(str(B)) > len(minsus[0]):
        return len(minsus)

    # 각 순열 값을 숫자로 만들고 비교
    for minsu in range(len(minsus) - 1, -1, -1):
        gold = ''
        for m in minsus[minsu]:
            gold += m

        # B보다 작거나 같은 값을 찾으면 거기까지의 길이를 넣기
        if B >= int(gold):
            return len(minsus[:minsu + 1])

    # B보다 작거나 같은 값이 없으면 0 반환
    else:
        return 0


# 자연수 A, B
A, B = map(int, input().split())
# 금민수
gold_minsu = ['4', '7']
# 금민수의 개수
answer = 0
# 시작점을 찾았는지 여부
flag = False
# A의 길이부터 B의 길이까지 중복 순열 만들기
for length in range(len(str(A)), len(str(B)) + 1):
    minsus = list(product(gold_minsu, repeat=length))

    # 시작점과 끝점의 자리 수가 같을 때
    if len(str(A)) == len(str(B)):
        answer += count_same_minsu(A, B, minsus)

    # 금민수 시작점 찾기
    elif not flag:
        flag = True
        answer += count_start_minsu(A, minsus)

    # 금민수 끝점 찾기
    elif flag:
        answer += count_end_minsu(B, minsus)

print(answer)