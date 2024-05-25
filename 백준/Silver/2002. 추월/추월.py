import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 추월 (2002)
 1. 대근: 차가 터널에 들어가는 순서대로 기록
 2. 영식: 차가 터널에서 나오는 순서대로 기록
[입력]
 1. N: 차의 대수
 2. N개의 줄: 대근 기록
 3. N개의 줄: 영식 기록
[출력]
 1. 터널 내부에서 반드시 추월했을 것으로 여겨지는 차가 몇 대?
"""

"""
<풀이>
 1. 일단 풀어보기
"""

N = int(input())

# 순서 기록
in_list = {}
out_list = {}

# 들어오는 순서 (차번호에 순서 기록)
for i in range(1, N + 1):
    car = input().rstrip()
    in_list[car] = i

# 나가는 순서 (순서에 차번호 기록)
for i in range(1, N + 1):
    car = input().rstrip()
    out_list[i] = car

# 추월 차량 탐색
overtaking = 0
for j in range(1, N):
    for k in range(j + 1, N + 1):
        # 순위 값이 더 큰 경우 추월한 차량으로 간주
        if in_list[out_list[j]] > in_list[out_list[k]]:
            overtaking += 1
            break

print(overtaking)