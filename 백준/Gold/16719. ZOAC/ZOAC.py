import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# ZOAC
1. 새로운 규칙으로 문자열을 보여줌
 - 아직 보여주지 않은 문자 중 추가했을 때의 문자열이 사전 순으로 가장 앞에 오도록 하기
 - ZOAC: A -> AC -> OAC -> ZOAC 순으로 보여줌
[입력]
1. 알파벳 대문자로 구성된 문자열이 주어짐
[출력]
1. 규칙에 맞게 순서대로 문자열 출력
"""

"""
<풀이>
1. 일단 풀어보기
2. 
A
AI
AIK
AINK
ALINK
ARLINK
ARTLINK
SARTLINK
STARTLINK
"""


# 문자열 추출
def extract(string, answer, now):
    # 문자열이 더 없으면 끝내기
    if not string:
        return

    # 사전 순으로 가장 앞선 문자열 찾기
    first = min(string)

    # 가장 앞선 문자열의 인덱스 번호 찾기
    index = string.index(first)

    # 가장 앞선 문자열의 실제 위치를 찾고 정답 배열에 넣고 출력
    answer[now + index] = first
    print("".join(answer))

    # 가장 앞선 문자열의 뒷쪽 문자열부터 붙이기
    extract(string[index + 1:], answer, now + index + 1)

    # 가장 앞선 문자열의 앞쪽 문자열 붙이기
    extract(string[:index], answer, now)


# 처음에 주어지는 문자열
string = list(input().rstrip())

# 정답 문자열
answer = [''] * len(string)

extract(string, answer, 0)

