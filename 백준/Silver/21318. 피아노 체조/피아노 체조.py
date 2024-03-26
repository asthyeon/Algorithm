import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 피아노 체조(21318)
 1. 피아노 체조: x번부터 y번까지의 악보를 번호 순서대로 연주하는 것
 2. i번보다 i+1번의 난이도가 더 높다면 실수함
[입력]
 1. N: 악보의 개수
 2. 두 번째 줄: 1 ~ N번까지 난이도
 3. Q: 질문 수
 4. Q개의 줄: x ~ y번까지 연주
[출력]
 1. x ~ y번 악보를 순서대로 연주할 때, 몇 개의 악보에서 실수하게 될지 출력
"""

"""
<풀이>
 1. 이중포문 -> 시간초과일듯
 2. 미리 실수한 위치들을 구해놓고 각 구간별 합을 구하기 -> 시간초과
 3. 실수한 위치들을 누적합으로 구하기
"""

# 악보의 수 N
N = int(input())
# 악보 정보
sheet_music = list(map(int, input().split()))

# 실수한 위치 파악(누적 합)
mistakes = [0] * N
for i in range(1, N):
    mistakes[i] = mistakes[i - 1]
    if sheet_music[i - 1] > sheet_music[i]:
        mistakes[i] += 1

# 질문 수 Q
Q = int(input())
# 질문 정보
for _ in range(Q):
    # 연주 순서 x번 ~ y번
    x, y = map(int, input().split())

    # 실수한 횟수 출력
    print(mistakes[y - 1] - mistakes[x - 1])


