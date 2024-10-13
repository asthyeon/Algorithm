import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 문자열 잘라내기 (2866)
 1. 테이블이 주어졌을 때 각 테이블의 열을 위에서 아래로 읽어서 하나의 문자열을 만듦
 2. 가장 위의 행을 지우며 문자열이 중복되지 않는다면 count의 개수를 1 증가시키는 과정 반복
 3. 동일한 문자열이 발견될 경우 반복을 멈추고 count의 개수 출력 후 프로그램 종료
[입력]
 1. R: 행 수, C: 열 수
 2. R개의 줄: C개의 알파벳 소문자가 주어짐
[출력]
 1. count 출력
"""

"""
<풀이>
 1. 일단 풀어보기 -> 시간초과
 2. 이분탐색
"""


def binary_search(strings):
    start = 0
    end = R - 1
    count = 0

    while start <= end:
        middle = (start + end) // 2
        # 중복확인용 변수
        duplication = False
        # 문자 만들기
        checks = set()
        for c in range(C):
            made = ''
            for r in range(middle, R):
                made += strings[r][c]
            # 중복되지 않았다면 세트에 넣기
            if made not in checks:
                checks.add(made)
            # 중복이라면 종료
            else:
                duplication = True
                break

        # middle 값 갱신
        if not duplication:
            start = middle + 1
            # 중복이 아닌 경우 답 갱신
            count = middle
        else:
            end = middle - 1

    return count


R, C = map(int, input().split())
# 문자열 정보 입력
strings = []
for _ in range(R):
    string = input().rstrip()
    strings.append(string)

print(binary_search(strings))