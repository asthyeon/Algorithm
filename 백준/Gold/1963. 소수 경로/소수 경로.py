import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 소수 경로
 1. 비밀번호를 한 번에 한 자리 밖에 못바꿈
 2. 네 자리 소수만 입력받음
 3. 바꾸는 과정에서도 항상 네 자리 소수임을 유지해야함
[입력]
 1. T: 테스트 케이스 수
 2. 다음 T줄에 걸쳐 각 줄에 1쌍씩 네 자리 소수가 주어짐
[출력]
 1. 두 소수 사이의 변환에 필요한 최소 회수 출력
 2. 불가능할시 Impossible 출력
"""

"""
(풀이)
 1. 네 자리 소수 미리 구하기
 2. 힙큐로 변환 횟수도 함께 저장
"""
import heapq
checks = [True] * 10000


# 에라토스테네스의 체
def era(checks):
    # 시작 수
    start = 2
    while True:
        # 현재 수의 배수는 모두 False로 바꾸기
        for i in range(start, 10000, start):
            if i == start:
                continue

            if checks[i]:
                checks[i] = False

        # 현재 수의 다음 수 중 True 값을 찾고 while문 반복
        for i in range(start + 1, 10000):
            if checks[i]:
                start = i
                break
        # 범위를 벗어난 경우 종료
        else:
            break


# 자리 값 바꿔보기
def change(A, B):
    # 힙큐
    hq = []
    # 시작 수 인큐
    heapq.heappush(hq, (0, A))
    # 시작 수 중복에 넣기
    duple.add(A)

    while hq:
        cnt, new_A = heapq.heappop(hq)

        # B와 맞는지 확인
        if new_A == B:
            return cnt

        # 자리 바꿔서 인큐
        for site in range(4):
            for change in range(10):
                # 첫번째 자리에 0이 들어가는 것을 막기
                if site == 0:
                    if change == 0:
                        continue

                # 문자 합치기
                join_A = join(site, change, new_A)

                # 소수가 맞는지 확인
                if not checks[int(join_A)]:
                    continue

                # 중복 체크
                if join_A in duple:
                    continue

                # B와 맞는지 확인
                if join_A == B:
                    return cnt + 1

                # 인큐 및 중복처리
                heapq.heappush(hq, (cnt + 1, join_A))
                duple.add(join_A)

    # 불가능할 시 Impossible 출력
    return "Impossible"


# 문자 합치기
def join(site, change, string):
    if site == 0:
        return str(change) + string[1] + string[2] + string[3]
    elif site == 1:
        return string[0] + str(change) + string[2] + string[3]
    elif site == 2:
        return string[0] + string[1] + str(change) + string[3]
    else:
        return string[0] + string[1] + string[2] + str(change)


# 네 자리 소수 구하기
era(checks)

T = int(input())
for tc in range(1, T + 1):
    # 두 소수 A, B
    A, B = map(str, input().split())

    # 중복체크용 세트
    duple = set()

    print(change(A, B))

