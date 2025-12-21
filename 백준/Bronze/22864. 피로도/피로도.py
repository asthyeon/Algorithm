import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 피로도 (22864)
1. 한 시간 일하면, 피로도는 +A, 일은 +B
2. 한 시간 쉬면, 피로도 -C, 음수로 내려가면 0
3. 피로도를 최대한 M을 넘지 않게 일하기
4. 하루는 24시간

[풀이]
1. 
"""


def work():
    task = 0
    condition = 0

    # 24시간
    for i in range(24):
        # 번아웃
        if condition > M:
            return 0
        # 일이 가능한 경우 일
        if A + condition <= M:
            condition += A
            task += B
        # 일이 불가능한 경우 휴식
        else:
            condition -= C
            # 음수 초기화
            if condition < 0:
                condition = 0

    return task


A, B, C, M = map(int, input().split())

print(work())