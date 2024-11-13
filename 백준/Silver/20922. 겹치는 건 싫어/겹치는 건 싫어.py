import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 겹치는 건 싫어 (20922)
 1. 수열에서 같은 원소가 K개 이하로 들어 있는 최장 연속 부분 수열의 길이 구하기
[입력]
 1. N: 수열의 길이, K: 같은 원소 허용 개수
 2. a: 수열
[출력]
 1. 조건을 만족하는 최장 연속 부분 수열의 길이 출력
"""

"""
<풀이>
 1. 투 포인터
"""


def two_pointer(a):
    # 시작점과 끝점
    start = 0
    end = 0
    # 정답 길이, 현재 길이 및 같은 원소 개수
    answer = 0
    now = 0
    same = {}

    while end < N:
        # 이번 원소 추가
        if a[end] not in same:
            same[a[end]] = 1
        else:
            same[a[end]] += 1

        # 같은 원소가 K개 이하일 때
        if same[a[end]] <= K:
            # 끝점 늘리기 및 현재 길이 늘리기, 정답 교체
            end += 1
            now += 1
            answer = max(answer, now)
        # 같은 원소가 K개 초과일 때
        else:
            # 시작점 및 끝점 제거 및 현재 길이 줄이기, 시작점 늘리기
            same[a[start]] -= 1
            same[a[end]] -= 1
            now -= 1
            start += 1

    return answer


N, K = map(int, input().split())
a = list(map(int, input().split()))

print(two_pointer(a))