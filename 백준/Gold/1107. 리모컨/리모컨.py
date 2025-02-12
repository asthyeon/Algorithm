import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 리모컨 (1107)
 1. 리모컨에는 버튼이 0~9, +, -가 있음
 2. 채널 0에서 -를 누르면 변하지 않음
 3. 지금 보고 있는 채널은 100번
[입력]
 1. N: 수빈이가 이동하려고 하는 채널
 2. M: 고장난 버튼의 개수
 3. 고장난 버튼이 있는 경우 셋째 줄에는 고장난 버튼이 주어짐
[출력]
 1. N으로 이동하기 위해 버튼을 최소 몇 번 눌러야 하는 지
"""

"""
<풀이>
 1. 브루트포스
"""

N = int(input())
M = int(input())
broken = set(map(str, input().split()))

# +, - 로만 이동하는 경우가 최대값
answer = abs(100 - N)
# 제일 큰 수에서 내려오는 경우 고려 (100 -> 500,000 or 999,900 -> 500,000)
for number in range(999901):
    for num in str(number):
        # 해당 채널 번호를 눌러서 만들 수 없다면 멈추기
        if num in broken:
            break
    # 해당 채널 번호를 눌러서 만들 수 있는 경우
    else:
        # (기존 값) vs (해당 채널 번호 누른 횟수) + (해당 채널 번호에서 +, - 로 가는 횟수)
        answer = min(answer, len(str(number)) + abs(number - N))

print(answer)