import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 보석 상자 (2792)
 1. 각각의 보석은 M가지 서로 다른 색상 중 한 색상
 2. 모든 보석을 N명의 학생들에게 나누어 주어야 함
 3. 이 때 보석을 받지 못하는 학생이 있어도 됨, 하지만 학생은 항상 같은 색상의 보석만
 4. 한 아이가 너무 많은 보석을 가져가면 다른 아이들이 질투함
 5. 질투심은 가장 많은 보석을 가져간 학생이 가지고 있는 보석의 개수
[입력]
 1. N: 아이들의 수, M: 색상의 수
 2. M개의 줄: K번째 줄에 주어지는 숫자는 K번 색상 보석의 개수
[출력]
 1. 질투심의 최솟값 출력
"""

"""
<풀이>
 1. 일단 풀어보기 -> 이분 탐색
 2. 한 학생이 가져갈 보석의 수를 탐색
 3. ZeroDivisionError 주의
"""


# 이분 탐색
def binary_search(jewels):
    start = 1
    end = max(jewels)

    while start <= end:
        mid = (start + end) // 2

        # 나눠받을 수 있는 학생 수
        students = 0
        for jewel in jewels:
            # 딱 나누어 떨어지면 그 만큼 학생 추가
            if jewel % mid == 0:
                students += jewel // mid
            # 딱 나누어 떨어지지 않으면 한 명이 더 받은 것
            else:
                students += (jewel // mid) + 1

        # 학생들이 더 많다면 보석 개수 늘리기
        if students > N:
            start = mid + 1
        # 그렇지 않다면 보석 개수 최소화
        else:
            end = mid - 1

    # 제일 많이 가져간 사람 반환
    return start


N, M = map(int, input().split())
jewels = []
for _ in range(M):
    K = int(input())

    jewels.append(K)

# 이분 탐색을 위한 정렬
jewels.sort()

print(binary_search(jewels))