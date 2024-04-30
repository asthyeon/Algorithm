import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# KCPC (3758)
 1. 어떤 문제에 대한 풀이 제출시 0 ~ 100 사이의 점수 얻음
 2. 풀이를 제출한 팀의 ID, 문제 번호, 점수가 제출되는 시간 순서대로 저장
 3. 한 문제에 대한 풀이를 여러 번 제출 가능, 최고 점수가 최종 점수(제출 X -> 0점)
 4. 당신 팀의 최종 점수는 각 문제에 대해 받은 점수의 총합
 5. 당신의 순위는 (당신 팀보다 높은 점수를 받은 팀의 수) + 1
 6. 점수 동일시 규정
  (1) 최종 점수가 같은 경우, 풀이를 제출한 횟수가 적은 팀의 순위가 높음
  (2) 최종 점수도 같고 제출 횟수도 같은 경우, 마지막 제출 시간이 더 빠른 팀의 순위가 높음
 7. 동시에 제출되는 풀이는 없고, 모든 팀이 적어도 한 번은 풀이를 제출함
[입력]
 1. T: 테스트 데이터 수
 2. n: 팀 수, k: 문제 수, t: 당신 팀의 ID, m: 로그 엔트리 수
 3. m개의 줄: 각 풀이에 대한 정보가 제출되는 순서대로 주어짐
  - i: 팀 ID, j: 문제 번호, s: 획득한 점수
[출력]
 1. 서버의 로그가 주어졌을 때 당신 팀의 순위를 계산하라
"""

"""
<풀이>
 1. 일단 풀어보기 -> 딕셔너리, 정렬 이용
"""

T = int(input())
for tc in range(1, T + 1):
    # 팀 수 n, 문제 수 k, 당신 팀 ID t, 로그 엔트리 수 m
    n, k, t, m = map(int, input().split())

    # 팀 딕셔너리
    teams = {}

    # 마지막 제출 순서
    last = 0

    for _ in range(m):
        last += 1
        # 팀 ID i, 문제 번호 j, 획득한 점수 s
        i, j, s = map(int, input().split())

        # 각 팀의 문제 점수 기록
        if i not in teams:
            teams[i] = {'cnt': 1, 'last': last, j: s}
        else:
            # 풀이를 제출한 횟수
            teams[i]['cnt'] += 1
            # 마지막 제출 순서
            teams[i]['last'] = last
            # 문제 점수 기록
            if j not in teams[i]:
                teams[i][j] = s
            else:
                teams[i][j] = max(teams[i][j], s)

    # 각 팀 점수(총 점수, 제출 횟수, 마지막 제출 순서, 팀 번호)
    scores = [[0, 10e9, 10e9, num] for num in range(n + 1)]

    # 팀 순회
    for team in teams:
        scores[team][1] = teams[team]['cnt']
        scores[team][2] = teams[team]['last']
        # 문제 순회
        for kind in teams[team]:
            if kind == 'cnt' or kind == 'last':
                continue
            # print(f' team: {team} number: {kind}, score: {teams[team][kind]}')
            scores[team][0] += teams[team][kind]

    # 총 점수(내림차순), 제출 횟수(오름차순), 마지막 제출 순서(오름차순) 정렬
    scores.sort(key=lambda x: (-x[0], x[1], x[2]))

    # 순위 출력
    for rank in range(n):
        if scores[rank][3] == t:
            print(rank + 1)
            break
