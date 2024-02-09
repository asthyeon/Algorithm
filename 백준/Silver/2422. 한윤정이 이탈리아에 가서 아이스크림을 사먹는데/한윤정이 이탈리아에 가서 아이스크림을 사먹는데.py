import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 한윤정이 이탈리아에 가서 아이스크림을 사먹는데(2422)
 1. 섞어먹으면 안되는 조합을 피하고 3가지 선택하는 경우의 수 구하기
[입력]
 1. N: 아이스크림 종류의 수, M: 섞어먹으면 안되는 조합의 개수
 2. 섞어먹으면 안되는 조합의 번호(같은 조합은 중복 X)
[출력]
 1. 가능한 방법이 총 몇 개 있는지? 
"""

"""
<풀이>
 1. 조합 이용
 2. 피해야 하는 조합이 2가지라고만 생각하기
 3. 리스트로 하면 시간 초과 -> 딕셔너리 안에 세트로 각 번호와 피해야 할 것들을 만들기
"""

from itertools import combinations


# 가능한 조합 구하기
def possible(tasteless):
    # 전체 조합
    total = list(combinations(ice_creams, 3))

    # 맛있는 조합
    delicious = 0

    # 전체 조합 순회
    for one in total:
        # 3번의 절차 검사(각 숫자가 한 숫자로 이루어진 피해야 할 조합에 담겨 있는지 확인)
        if one[0] in tasteless:
            if one[1] in tasteless[one[0]] or one[2] in tasteless[one[0]]:
                continue
        if one[1] in tasteless:
            if one[0] in tasteless[one[1]] or one[2] in tasteless[one[1]]:
                continue
        if one[2] in tasteless:
            if one[0] in tasteless[one[2]] or one[1] in tasteless[one[2]]:
                continue

        delicious += 1

    return delicious


# 아이스크림의 종류 N, 섞어먹으면 안되는 조합의 개수 M
N, M = map(int, input().split())
# 아이스크림 종류 만들기
ice_creams = [i for i in range(1, N + 1)]
# 맛없는 조합 만들기
tasteless = {}
for _ in range(M):
    ice = tuple(map(int, input().split()))

    # 각 번호와 피해야 할 것들 조합(딕셔너리 안에 세트로 담기)
    if ice[0] not in tasteless:
        tasteless[ice[0]] = {ice[1]}
    else:
        tasteless[ice[0]].add(ice[1])

    if ice[1] not in tasteless:
        tasteless[ice[1]] = {ice[0]}
    else:
        tasteless[ice[1]].add(ice[0])

print(possible(tasteless))