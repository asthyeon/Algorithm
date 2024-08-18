import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 귀여운 라이언 (15565)
 1. 인형이 N개 일렬로 놓여 있음
 2. 라이언은 1, 어피치는 2
[입력]
 1. N: 인형 수, K: 구해야 할 가장 작은 연속된 인형들의 집합의 크기
 2. N개의 인형의 정보
[출력]
 1. K개 이상의 라이언 인형을 포함하는 가장 작은 연속된 인형들의 집합의 크기 출력
 2. 그런 집합이 없다면 -1 출력
"""

"""
<풀이>
 1. 투 포인터
"""

N, K = map(int, input().split())
dolls = list(map(int, input().split()))

# 시작과 끝점(K개 이상이므로 끝점은 K - 1)
start = 0
end = K - 1
# 현재 구간에서 라이언 인형 세기
lion = 0
for i in range(K):
    if dolls[i] == 1:
        lion += 1
# 가장 작은 연속된 인형들의 집합의 크기
minimum = 10e9

# 포인터 이동
while end < N:

    # 라이언이 k개 이상이라면 집합 크기 갱신
    if lion >= K:
        minimum = min(minimum, end - start + 1)
        # 앞칸 이동 전 라이언 개수 줄이기
        if dolls[start] == 1:
            lion -= 1
        # 앞칸 이동
        start += 1

    # 라이언이 k개 미만이라면
    else:
        # 뒷칸 이동
        end += 1
        # 범위를 벗어날시 반복 종료
        if end >= N:
            break
        # 뒷칸 이동 후 라이언이라면 개수 늘리기
        if dolls[end] == 1:
            lion += 1

# 정답 출력
if minimum == 10e9:
    print(-1)
else:
    print(minimum)
