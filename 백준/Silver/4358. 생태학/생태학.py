import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 생태학 (4358)
 1. 미국 전역의 나무들이 주어졌을 때 각 종이 전체에서 몇 %를 차지하는지 구하기
[입력]
 1. 한 줄에 하나의 나무 종 이름
 2. 최대 10,000 ~ 1,000,000 그루의 나무가 주어짐
[출력]
 1. 주어진 각 종의 이름을 사전순으로 출력
 2. 그 종이 차지하는 비율을 백분율로 소수점 4째자리까지 반올림해 함께 출력
"""

"""
<풀이>
 1. 세트로 중복제거, 딕셔너리로 카운트
 2. round -> 십진 소수가 float로 정확히 표현될 수 없으므로 값이 다를 수 있음
 3. f-string으로 나타내기
"""

# 중복, 퍼센트, 사전, 총 숫자
species = set()
percentage = {}
dictionary = []
total = 0

while True:
    # 입력받기
    tree = input().rstrip()

    # 공백을 입력받는 경우 종료
    if not tree:
        break

    # 처음 들어오는 종이라면 중복 추가, 퍼센트 추가, 사전 추가
    if tree not in species:
        species.add(tree)
        dictionary.append(tree)
        percentage[tree] = 1

    # 처음이 아니라면 퍼센트만 추가
    else:
        percentage[tree] += 1

    # 총 숫자 추가
    total += 1

# 사전 순 정렬
dictionary.sort()

# 하나씩 출력
for name in dictionary:
    percent = percentage[name] / total * 100
    print(f'{name} {percent:.4f}')
