import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 사다리 타기 (2469)
 1. 사다리 타기 구현
 2. 두 가로 막대가 직접 연결되는 일은 없음
 3. 가로 막대가 없는 경우: '*', 있을 경우: '-'
 4. 하나의 가로 줄이 감추어치는데, 감추어진 특정 가로 줄: 길이 k-1, '?'
[입력]
 1. k: 참가한 사람의 수
 2. n: 가로 막대가 놓일 전체 가로 줄의 수
 3. 세번째 줄: 참가자들의 최종 순서가 길이 k인 대문자 문자열
 4. n개의 줄: 사다리 정보
[출력]
 1. 지정한 도착순서가 만들어질 수 있도록 감추어진 가로 줄 구성
   (어떻게 구성해도 원하는 순서를 얻을 수 없는 경우 'x'로만 구성된 길이 k-1 문자열 출력
"""

"""
<풀이>
 1. 구현
 2. 감춰진 줄 사이를 두고 나누기
"""

k = int(input())
n = int(input())
arrived = list(input().rstrip())
ladder = [list(input().rstrip()) for _ in range(n)]

# 시작 문자열
started = sorted(arrived)
# 감춰진 줄을 기준으로 윗 부분, 아랫 부분 나누기
upside = []
downside = []
standard = False
for line in range(n):
    # 기준 찾기
    if '?' in ladder[line]:
        standard = True
        continue
    # 기준에 따라 부분 나누기
    if not standard:
        upside.append(ladder[line])
    else:
        downside.append(ladder[line])

# 윗 부분 줄타고 내려가기
for ux in range(len(upside)):
    for uy in range(k - 1):
        # 가로 막대가 있는 경우 자리 교체
        if upside[ux][uy] == '-':
            started[uy], started[uy + 1] = started[uy + 1], started[uy]
# 아랫 부분 줄타고 올라가기
for dx in range(len(downside) - 1, -1, -1):
    for dy in range(k - 1):
        # 가로 막대가 있는 경우 자리 교체
        if downside[dx][dy] == '-':
            arrived[dy], arrived[dy + 1] = arrived[dy + 1], arrived[dy]

# 정답 만들기
answer = ''
for i in range(k - 1):
    # 앞뒤가 서로 반대라면 가로 막대 추가
    if started[i] == arrived[i + 1] and started[i + 1] == arrived[i]:
        answer += '-'
        started[i], started[i + 1] = started[i + 1], started[i]
    # 그게 아니라면 별표 추가
    else:
        answer += '*'

# 시작과 도착이 같다면 정답 출력
if started == arrived:
    print(''.join(answer))
# 시작과 도착이 다르다면 'x' 출력
else:
    print('x' * (k - 1))
