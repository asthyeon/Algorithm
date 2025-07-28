import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 문자열 교환 (1522)
1. a와 b로만 이루어진 문자열이 주어질 때, a를 모두 연속으로 만들기 위해 필요한 교환의 회수?
2. 문자열은 원형(처음과 끝이 인접)
3. 투 포인터
 - a 전체 개수 만큼의 윈도우 -> 윈도우에 포함되지 못한 a의 개수 = 교환 수
"""

string = input().rstrip()
# 전체 a의 개수
cnt_a = 0
for s in string:
    if s == 'a':
        cnt_a += 1

# 최댓값 및 전체 길이
maximum = 0
for i in range(cnt_a):
    if string[i] != 'a':
        maximum += 1
length = len(string)
# 투포인터
cnt = maximum
for start in range(1, length):
    # 끝점
    end = (start + cnt_a - 1) % length

    # 지난 값이 a가 아니면 개수 -1, 마지막 값이 a가 아니면 개수 +1
    if string[start - 1] != 'a':
        cnt -= 1
    if string[end] != 'a':
        cnt += 1
    # 값 갱신
    maximum = min(maximum, cnt)

print(maximum)


