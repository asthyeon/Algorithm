import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 과일 탕후루 (30804)
 1. 과일 탕후루를 두 종률 이하로 사용해서 만들어야 함
 2. 막대의 앞쪽과 뒤쪽에서 몇 개의 과일을 빼서 두 종류 이하의 과일만 남기기
[입력]
 1. N: 과일의 개수
 2. S: 탕후루에 꽂힌 과일들
[출력]
 1. 과일을 두 종류 이하로 사용한 탕후루 중, 과일의 개수가 가장 많은 탕후루의 과일 개수 출력
"""

"""
<풀이>
 1. 투 포인터
 2. 세트 -> 이전 과일이 중복인 경우 제거 불가 -> 딕셔너리
"""


def two_pointer(S):
    start = 0
    end = 0

    # 정답과 가짓수, 현재 과일의 개수
    answer = 0
    kind = {}

    while end < N:
        # 이번 과일 집어 넣기
        if S[end] not in kind:
            kind[S[end]] = 1
        else:
            kind[S[end]] += 1

        # 가짓수가 2가지 이하라면
        if len(kind) <= 2:
            # 값 갱신
            answer += 1
            end += 1

        # 가짓수가 2가지 초과라면
        else:
            # 이전 과일 제거
            kind[S[start]] -= 1
            if kind[S[start]] == 0:
                kind.pop(S[start])
            # 값 갱신
            start += 1
            end += 1

    return answer


N = int(input())
S = list(map(int, input().split()))

print(two_pointer(S))