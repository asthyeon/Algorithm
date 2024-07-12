import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 다이어트 (1484)
 1. G킬로그램: 성원이의 현재 몸무게의 제곱에서 성원이가 기억하고 있던 몸무게의 제곱을 뺀 것
 2. 성원이의 현재 몸무게로 가능한 것을 모두 출력하기
[입력]
 1. 첫째 줄: G가 주어짐
[출력]
 1. 한 줄에 하나씩 가능한 성원이의 현재 몸무게를 오름차순으로 출력
 2. 가능한 몸무게가 없을 때는 -1 출력
 3. 몸무게가 자연수로 떨어지지 않을 때는 제외
"""

"""
<풀이>
 1. 수학
4 x 4 = 16 - 1 x 1 = 15
8 x 8 = 64 - 7 x 7 = 15
 2. G의 제곱근보다 큰 자연수부터 
"""


# 기억하고 있는 최소 몸무게의 제곱근 구하기
def remember(origin):
    return int((origin - G) ** (1 / 2))


G = int(input())
# 제곱근보다 큰 자연수
natural = int(G ** (1 / 2) + 1)
# 기억하고 있는 최소 몸무게의 제곱근
memory = remember(natural ** 2)
# 정답 리스트
answers = []

while True:
    weight = (natural ** 2) - (memory ** 2)

    # 차이가 G보다 클 때
    if weight > G:
        # 현재 몸무게와 기억 몸무게의 차이가 1일때 종료
        if natural - memory == 1:
            break
        # 현재 몸무게 증가 및 기억 몸무게 갱신
        natural += 1
        memory = remember(natural ** 2)

    # 정답이 일치한다면 리스트에 넣고 값 증가
    elif weight == G:
        answers.append(natural)
        natural += 1
        memory = remember(natural ** 2)

    # 정답이 아니라면
    else:
        # 기억하고 있는 몸무게 증가
        memory += 1

# 정답이 있으면 출력
if answers:
    for answer in answers:
        print(answer)
# 정답이 없으면 -1 출력
else:
    print(-1)
