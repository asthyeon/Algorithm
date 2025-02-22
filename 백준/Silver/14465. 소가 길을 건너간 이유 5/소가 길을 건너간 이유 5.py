import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K, B = map(int, input().split())
stoplights = [i for i in range(1, N + 1)]
for j in range(B):
    broken = int(input())
    stoplights[broken - 1] = 0

# 최초 K개의 신호등에서 고장난 것 확인(최대값)
answer = 0
for k in range(K):
    if not stoplights[k]:
        answer += 1

# 현재 윈도우에서 고장난 개수는 최초 값과 같음
window = answer
# 윈도우 옮기기
for l in range(N - K):
    # 맨 앞이 고장난 것이면 수리 대상 제외
    if not stoplights[l]:
        window -= 1
    # 맨 뒤가 고장난 것이면 수리 대상 포함
    if not stoplights[K + l]:
        window += 1

    # 최솟값 교체
    answer = min(answer, window)

print(answer)
