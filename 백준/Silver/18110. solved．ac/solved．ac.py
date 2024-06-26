import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# solved.ac (18110)
 1. 난이도 결정 방식
  - 아직 아무 의견이 없다면 문제의 난이도는 0
  - 의견이 하나 이상 있다면, 문제의 난이도는 모든 사람의 난이도 의견의 30% 절사평균
 2. 절사평균
  - 가장 큰 값들과 가장 작은 값들을 제외하고 평균을 내는 것
  - 30% 절사평균: 위에서 15%, 아래에서 15%를 각각 제외하고 평균 계산
 3. 제외되는 사람의 수는 위 아래에서 각각 반올림
 4. 계싼된 평균도 정수로 반올림
[입력]
 1. n: 의견의 개수
 2. n개의 줄: 사용자들이 제출한 난이도
[출력]
 1. 문제의 난이도 출력
"""

"""
<풀이>
 1. 수학
 2. 반올림 때 round 쓰지 말기 -> f-string
"""

n = int(input())
# 0일 때 제외
if n == 0:
    print(0)

else:
    # 의견 취합
    opinions = []
    for _ in range(n):
        opinion = int(input())

        opinions.append(opinion)

    # 의견 정렬
    opinions.sort()
    # 난이도
    difficulty = 0

    # 반올림 수 -> 2번째에서 반올림하기
    rounds = n * 0.15
    # 직접 반올림 계산
    if rounds - int(rounds) >= 0.5:
        rounds = int(rounds) + 1
    else:
        rounds = int(rounds)
    # 인원 합계
    people = n - (rounds * 2)
    # 점수 합계
    point = sum(opinions[rounds:n - rounds])

    # 정답 출력
    answer = point / people
    if answer - int(answer) >= 0.5:
        answer = int(answer) + 1
    else:
        answer = int(answer)
    print(answer)