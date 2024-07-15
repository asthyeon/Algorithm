import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 선발 명단 (3980)
 1. 뛸 선발 선수 11명은 미리 골라두었지만, 어떤 선수를 어느 포지션에 배치해야 할지 아직 결정 X
 2. 각각의 포지션에서의 능력을 0부터 100까지의 정수로 수치화 함
 3. 모든 포지션에 선수를 배치해야 하고, 각 선수는 능력치가 0인 포지션에 배치 X
[입력]
 1. C: 테스트 케이스 개수
 2. 각각의 케이스는 11줄로 이루어짐, i번 줄은 0과 100 사이의 11개 정수 Sij를 포함
 3. Sij는 i번 선수가 j번 포지션에서 뛸 때의 능력
 4. 모든 선수에게 적합한 포지션의 수는 최대 5개(0보다 큼)
[출력]
 1. 모든 포지션의 선수를 채웠을 때, 능력치의 합의 최댓값을 한 줄에 하나씩 출력
"""

"""
<풀이>
 1. 백트래킹
"""


# 백트래킹
def back_tracking(number, grade):
    global answer
    # 선수가 다 쓰였다면 능력치 합 갱신
    if number == 11:
        answer = max(answer, grade)
        return

    for j in range(11):
        # 방문하지 않고 0이 아니라면
        if not visited[j] and players[number][j]:
            # 방문 처리
            visited[j] = 1
            # 백트래킹
            back_tracking(number + 1, grade + players[number][j])
            # 방문 취소
            visited[j] = 0


C = int(input())
for tc in range(1, C + 1):
    # 선수들
    players = []
    for i in range(11):
        player = list(map(int, input().split()))
        players.append(player)

    # 방문 리스트
    visited = [0] * 11
    # 능력치 합
    answer = 0
    # 능력치 합치기 (선수 번호, 점수)
    back_tracking(0, 0)
    print(answer)