import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# A와 B 2 (12919)
 1. 가능한 연산 두가지
  - 문자열의 뒤에 A 추가
  - 문자열의 뒤에 B 추가 및 문자열 뒤집기
[입력]
 1. S: 기본 문자열
 2. T: 바꿔야 될 문자열
[출력]
 1. S를 T로 바꿀 수 있으면 1, 없으면 0 출력
"""

"""
<풀이>
 1. 브루트포스 -> 시간 초과
 2. T -> S 역순으로 바꿔보기
"""


def brute_force(string):
    # 정답 체크
    if string == S:
        print(1)
        exit()
    # 정답이 아닐 때(마지막 경우의 수까지 확인해야 하므로 exit이 아닌 return)
    elif len(string) == 0:
        return 0

    # 맨 뒤가 'A' 일 때 제거
    if string[-1] == 'A':
        brute_force(string[:-1])
    # 맨 앞이 'B' 일 때 제거 후 뒤집기
    if string[0] == 'B':
        brute_force(string[1:][::-1])

    # 정답이 아닐 때
    return 0


S = input().rstrip()
T = input().rstrip()

print(brute_force(T))