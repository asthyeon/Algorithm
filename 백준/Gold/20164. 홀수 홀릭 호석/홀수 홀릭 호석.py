import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 홀수 홀릭 호석 (20164)
 1. 가지고 있는 수 N을 일련의 연산을 거치면서 등장하는 숫자들에게 홀수를 최대한 많이 보고 싶음
 2. 연산 순서
  - 수의 각 자리 숫자 중에서 홀수의 개수를 종이에 적는다
  - 수가 한 자리이면 더 이상 아무것도 하지 못하고 종료
  - 수가 두 자리이면 2개로 나눠서 합을 구하여 새로운 수로 생각
  - 수가 세 자리 이상이면 임의의 위치에서 끊어서 3개의 수로 분할 및 3개를 더한 값을 새로운 수로
 3. 최종값: 연산이 종료된 순간에 종이에 적힌 수들을 모두 더하기
[입력]
 1. N: 처음 시작할 때 가지고 있는 수
[출력]
 1. 호석이가 만들 수 있는 최종값 중 최솟값과 최댓값 구분하여 출력
"""

"""
<풀이>
 1. 일단 풀어보기
"""


# 연산
def calculator(N, paper):
    global maximum, minimum
    # 새로운 종이에 홀수의 개수 적기
    new_paper = []
    cnt = 0
    for i in range(len(N)):
        # 홀수라면 카운트
        if int(N[i]) % 2 == 1:
            cnt += 1
    new_paper.append(cnt)

    # 1자리일 때
    if len(N) == 1:
        # 종이 합치기
        paper += new_paper
        # 최솟값, 최댓값 갱신
        minimum = min(minimum, sum(paper))
        maximum = max(maximum, sum(paper))
    # 2자리일 때 2개로 나눈 숫자로 재귀
    elif len(N) == 2:
        calculator(str(int(N[0]) + int(N[1])), paper + new_paper)
    # 3자리 이상일 때
    else:
        # 임의의 위치에서 3개의 수로 분할후 재귀
        for j in range(1, len(N) - 1):
            for k in range(j + 1, len(N)):
                calculator(str(int(N[0:j]) + int(N[j:k]) + int(N[k:len(N) + 1])), paper + new_paper)


N = input().rstrip()

# 종이
paper = []
# 최댓값과 최솟값
maximum = 0
minimum = 10e9
# 연산
calculator(N, paper)
print(minimum, maximum)