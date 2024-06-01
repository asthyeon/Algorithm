import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 거북이 (8911)
 1. 거북이 로봇에게 내릴 수 있는 명령
  - F: 한 눈금 앞으로
  - B: 한 눈금 뒤로
  - L: 왼쪽으로 90도 회전 (방향만 회전)
  - R: 오른쪽으로 90도 회전 (방향만 회전)
 2. 거북이는 (0, 0) 에 있고, 북쪽을 쳐다보고 있음
 3. 거북이가 지나간 영역이 직사각형이 아닌 경우 넓이는 0
[입력]
 1. T: 테스트 케이스 수
 2. 명령
[출력]
 1. 거북이가 이동한 영역을 모두 포함하는 가장 작은 직사각형 넓이 출력
"""

"""
<풀이>
 1. 구현
 2. 거북이가 이동한 만큼의 최대 최소를 구하고 사각형 넓이 구하기
"""
# 동남서북
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


# 명령 수행
def perform(commands):
    # 현재 방향 (북)
    direction = 3
    # 현재 위치
    x = y = 0
    # 최대 최소 가로 세로 구하기
    max_x = min_x = max_y = min_y = 0

    for command in commands:
        # 앞으로 한 칸 이동
        if command == 'F':
            x += dirs[direction][0]
            y += dirs[direction][1]

        # 뒤로 한 칸 이동
        elif command == 'B':
            x -= dirs[direction][0]
            y -= dirs[direction][1]

        # 왼쪽 회전
        elif command == 'L':
            direction -= 1
            # 동쪽 방향일 경우 북쪽으로 초기화
            if direction == -1:
                direction = 3

        # 오른쪽 회전
        elif command == 'R':
            direction += 1
            # 북쪽 방향일 경우 동쪽으로 초기화
            if direction == 4:
                direction = 0

        # 최대 최소 가로 세로 저장
        max_x = max(max_x, x)
        min_x = min(min_x, x)
        max_y = max(max_y, y)
        min_y = min(min_y, y)

    # 사각형 넓이 구하기
    square = (max_x - min_x) * (max_y - min_y)
    return square


T = int(input())
for tc in range(1, T + 1):
    commands = input().rstrip()

    print(perform(commands))
