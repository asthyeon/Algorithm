import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 기타 레슨 (2343)
 1. 블루레이를 녹화할 때 강의의 순서가 바뀌면 안됨
 2. i번 강의와 j번 강의를 같은 블루레이에 녹화하려면 그 사이 모든 강의도 같은 블루레이 녹화
 3. 블루레이의 개수를 가급적으로 줄이려고 함
 4. 블루레이의 크기를 최소로 하기
[입력]
 1. N: 강의의 수, M: 블루레이 수
 2. 기타 강의의 길이가 강의 순서대로 주어짐
[출력]
 1. 가능한 블루레이 크기중 최소
"""

"""
<풀이>
 1. 이분탐색
 2. 블루레이들 중 가장 큰 값을 출력해야 함
"""


# 이분탐색
def binary_search(lessons):
    # 시작지점은 각 강의중 가장 큰 값
    start = max(lessons)
    # 끝지점은 전체 강의의 합
    end = sum(lessons)
    answer = 0

    while start <= end:
        middle = (start + end) // 2

        # 블루레이 개수와 하나당 크기
        cnt = 1
        size = middle
        # 강의 순회
        for lesson in lessons:

            size -= lesson
            # 이번 블루레이가 용량을 감당하지 못하면
            if size < 0:
                # 새로운 블루레이 추가
                cnt += 1
                size = middle - lesson

        # 블루레이 허용 개수보다 클 경우 줄이기
        if cnt > M:
            start = middle + 1
        # 블루레이 허용 개수보다 작거나 같은 경우 늘리기
        else:
            answer = middle
            end = middle - 1

    return answer


N, M = map(int, input().split())
lessons = list(map(int, input().split()))

print(binary_search(lessons))