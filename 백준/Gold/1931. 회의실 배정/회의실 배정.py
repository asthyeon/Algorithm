import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 회의실 배정 (1931)
1. 각 회의 I에 대해 시작시간과 끝나는 시간이 주어짐
2. 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수 찾기

[풀이]
1. 회의가 일찍 끝나는 순대로 진행하기
2. 회의 시작 시간도 정렬 추가
"""


# 회의 진행
def progress(meetings):
    cnt = 0
    end = 0
    for i in range(N):
        # 처음 끝나는 시간 지정
        if i == 0:
            end = meetings[i][1]
            cnt += 1
            continue

        # 바로 다음으로 진행 가능한 회의를 발견하면 회의 진행
        if meetings[i][0] >= end:
            end = meetings[i][1]
            cnt += 1

    return cnt


N = int(input())
meetings = list(tuple(map(int, input().split())) for _ in range(N))

# 끝나는 순서대로 정렬(그 다음 회의 시작 시간으로 정렬)
meetings = sorted(meetings, key=lambda x: (x[1], x[0]))

print(progress(meetings))
