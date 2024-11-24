import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 줄세우기 (10431)
 1. 키 작은 순서대로 번호 부여
  - 자기 앞에 더 큰 학생이 없으면 그냥 그 자리에 섬
  - 자기 앞에 더 큰 학생이 있다면 그 중 가장 앞의 학생(A) 앞에 섬
  - A부터 그 뒤 모든 학생들이 한 발씩 물러서게 됨
[입력]
 1. P: 테스트 케이스의 수
 2. heights: 테스트 케이스 번호와 학생들의 키
[출력]
 1. 테스트 케이스 번호와 학생들이 뒤로 물러난 걸음 수의 총합 출력
"""

"""
<풀이>
 1. 삽입 정렬
"""
from collections import deque

P = int(input())
for tc in range(1, P + 1):
    heights = list(map(int, input().split()))
    T, line = heights[0], deque(heights[1:])

    # 줄세운 리스트와 총 걸음 수
    line_up = deque()
    steps = 0
    for i in range(20):
        now = line.popleft()
        # 첫 번째
        if i == 0:
            line_up.append(now)
        # 첫 번째 외
        else:
            # 뒤에서부터 자신보다 크면 서기
            for j in range(i - 1, -1, -1):
                if line_up[j] < now:
                    line_up.insert(j + 1, now)
                    # 총 걸음 수 더하기
                    steps += i - (j + 1)
                    break
            # 내가 제일 작으면 맨 앞에 서기
            else:
                steps += i
                line_up.appendleft(now)

    print(T, steps)
