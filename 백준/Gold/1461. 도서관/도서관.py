import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 도서관 (1461)
 1. 세준이는 현재 0
 2. 0에 있는 각 책들의 원래 위치가 주어질 때, 모두 제자리에 놔둘 때 드는 최소 걸음 수 구하기
 3. 세준이는 한 걸음에 좌표 1칸씩 이동, 모두 놔둔 후 0으로 돌아올 필요 없음
 4. 한 번에 최대 M권의 책을 들 수 있음
[입력]
 1. N: 책의 개수, M: 한 번에 들 수 있는 책의 개수
 2. 둘째 줄: 각 책의 위치 (책의 위치는 0이 아님)
[출력]
 1. 정답 출력
"""

"""
<풀이>
 1. 정렬
 2. 양수, 음수를 나눠서 해보기
"""

N, M = map(int, input().split())
books = list(map(int, input().split()))
# 정렬
books.sort()

# 마지막 지점 구하기
if abs(books[0]) > abs(books[-1]):
    last = 0
else:
    last = N - 1

# 음수 부분과 양수 부분 구하기
point = N
for i in range(N):
    # 양수가 되는 부분을 기준 점으로 잡고 종료
    if books[i] > 0:
        point = i
        break
minus = books[:point]
plus = books[point:]

# 갯수 세기
cnt = 0
# 왼쪽에서 시작
for left in range(0, len(minus), M):
    cnt -= minus[left] * 2
# 오른쪽에서 시작
for right in range(len(plus) - 1, -1, -M):
    cnt += plus[right] * 2

# 마지막 값은 한 번 빼주기
print(cnt - abs(books[last]))

