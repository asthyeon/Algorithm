import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 문자열 게임 2 (20437)
1. 게임진행방식
 1) 소문자로 이루어진 문자열 W가 주어짐
 2) 양의 정수 K가 주어짐
 3) 어떤 문자를 K개 포함하는 가장 짧은 연속 문자열의 길이 구하기
 4) 어떤 문자를 K개 포함하고, 문자열의 처음과 마지막이 같은 가장 긴 연속 문자열 길이 구하기
2. 브루트포스 -> 전체를 검사하기에 시간초과
3. 슬라이딩 윈도우 사용, 각 알파벳이 나오는 번호 구해보기
"""

T = int(input())
for tc in range(1, T + 1):
    W = input().rstrip()
    K = int(input())
    minimum = 10001
    maximum = 0

    # 각 알파벳이 나오는 위치 구하기
    locations = {}
    for i in range(len(W)):
        if W[i] not in locations:
            locations[W[i]] = []
        locations[W[i]].append(i)

    # 각 알파벳 리스트 순회
    for alphabet in locations:
        cnt = len(locations[alphabet])
        # 조건을 만족한다면
        if cnt >= K:
            for l in range(cnt - K + 1):
                # 길이 구하기 및 값 갱신
                length = locations[alphabet][l + K - 1] - locations[alphabet][l] + 1
                minimum = min(minimum, length)
                maximum = max(maximum, length)

    if minimum == 10001:
        print(-1)
    else:
        print(minimum, maximum)
