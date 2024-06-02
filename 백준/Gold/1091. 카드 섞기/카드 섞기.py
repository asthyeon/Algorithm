import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 카드 섞기 (1091)
 1. 카드를 섞을 때 주어진 방법을 이용해서만 섞을 수가 있음
  - 길이가 N인 수열 S로 주어짐
  - 카드를 한 번 섞고 나면 i번째 위치에 있던 카드는 S[i]번째 위치로 이동
 2. [0, 1, 2] 플레이어 위치 고정 -> [0, 1, 2, 0, 1, 2] 반복
 2. 맨 처음 i번째 위치에 있던 카드를 최종적으로 플레이어 P[i]에게 보내기
[입력]
 1. N: 카드 수
 2. P: 각 플레이어에게 보내야 하는 길이가 N인 수열
 3. S: 섞을 때 위치가 변하게 되는 길이가 N인 수열 
[출력]
 1. 카드 섞는 횟수의 최솟값 구하기
 2. 섞어도 카드를 해당하는 플레이어에게 줄 수 없다면 -1 출력
"""

"""
<풀이>
 1. 해석
P = [2, 0, 1]
S = [1, 2, 0]
0번 카드 -> P[0]번 - 2번 플레이어
1번 카드 -> P[1]번 - 0번 플레이어
2번 카드 -> P[2]번 - 1번 플레이어
 = [1, 2, 0]
  - 0번 플레이어에게 1번 카드
  - 1번 플레이어에게 2번 카드
  - 2번 플레이어에게 0번 카드
 2. P 값을 컨트롤
"""


# 카드 섞기
def shuffle(S, shuffling):
    # 카드 섞기
    for i in range(N):
        shuffling[S[i]] = P_copy[i]

    return shuffling


N = int(input())
P = list(map(int, input().split()))
S = list(map(int, input().split()))

# P 복사
P_copy = P[:]
# 카드 리스트
cards = [0, 1, 2] * (N // 3)
# 섞기용
shuffling = [0] * N
# 사용된 배열
used = set()
# 섞은 횟수
cnt = 0

# 카드 섞기
while True:
    # 이미 사용된 배열이라면 종료 (카드를 해당하는 플레이어에게 줄 수 없음)
    if tuple(P_copy) in used:
        print(-1)
        break
    # P 복제본이 카드 리스트와 같다면 종료
    if P_copy == cards:
        print(cnt)
        break

    # 횟수 추가
    cnt += 1
    # 현재 배열 추가
    used.add(tuple(P_copy))
    # 섞기
    shuffling = shuffle(S, shuffling)
    P_copy = shuffling[:]