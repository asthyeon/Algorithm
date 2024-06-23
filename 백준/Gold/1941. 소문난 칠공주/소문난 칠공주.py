import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 소문난 칠공주 (1941)
 0. 이다솜파 vs 임도연파
 1. 소문난 칠공주의 규칙
  - 7명의 여학생
  - 7명의 자리는 가로나 세로로 반드시 인접
  - 이다솜파의 학생이 적어도 4명 이상 포함
[입력]
 1. S: 이다솜파, Y: 임도연파의 정보가 5*5 형태로 주어짐
[출력]
 1. 소문난 칠공주를 결성할 수 있는 모든 경우의 수 출력
"""

"""
<풀이>
 1. 델타탐색으로 백트래킹 -> 다른 부분에서 시작하는 경우 고려 불가
 2. 지나온 부분을 q에 넣고 찾기 -> 이미 사용된 조합은 거르기
 3. visited의 형태를 1차원 배열로 만들기
"""


# 백트래킹
def back_tracinkg(students, q, visited, som, yeon):
    global answer
    global used
    # 조건 만족시 경우의 수 추가
    if som + yeon == 7 and som >= 4 and tuple(visited) not in used:
        answer += 1
        # 사용된 조합 추가
        used.add(tuple(visited))
        return
    # 조건 불만족인 경우 2개
    elif som + yeon >= 7:
        return
    elif yeon > 4:
        return

    # 큐 순회
    for sx, sy in q:
        # 델타 탐색
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = sx + dx, sy + dy
            # 벽 형성 및 미 방문한 곳이라면
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx * 5 + ny]:
                # 방문 처리
                visited[nx * 5 + ny] = 1
                # 다솜이 파
                if students[nx][ny] == 'S':
                    back_tracinkg(students, q + [(nx, ny)], visited, som + 1, yeon)
                # 도연이 파
                else:
                    back_tracinkg(students, q + [(nx, ny)], visited, som, yeon + 1)
                # 방문 처리 원상 복구
                visited[nx * 5 + ny] = 0


students = [list(map(str, input().rstrip())) for _ in range(5)]

# 모든 경우의 수
answer = 0
# 방문 리스트
visited = [0] * 25
# 큐
q = []
# 이미 사용된 조합
used = set()

# 칠공주 결성
for x in range(5):
    for y in range(5):
        # 방문 처리
        visited[x * 5 + y] = 1
        # 다솜파 시작
        if students[x][y] == 'S':
            back_tracinkg(students, [(x, y)], visited, 1, 0)
        # 도연파 시작
        else:
            back_tracinkg(students, [(x, y)], visited, 0, 1)
        # 방문 원상복귀
        visited[x * 5 + y] = 0

print(answer)