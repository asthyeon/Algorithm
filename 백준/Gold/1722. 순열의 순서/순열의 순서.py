import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 순열의 순서
 0. 1부터 N까지의 수를 임의로 배열한 순열은 총 N!
 1. 임의의 순열은 정렬 가능
 2. 앞의 숫자가 작은 것이 앞쪽
 3. k가 주어지면 k번째 순열, 임의의 순열이 주어지면 몇 번째 순열 인지 구하기
[입력]
 1. N
 2. 소문제 번호(1: k, 2: N개의 수)
[출력]
 1. k번째 수열을 나타내는 N개의 수 or 몇 번째 순열 인지 출력
"""

"""
<풀이>
 1. 순열 이용 -> 메모리 초과
 2. 직접 만들어보기
  - 앞자리 수마다 가지는 가지 수 = 전체 / N
  - 앞자리 수 = (k / (앞자리 수마다 가지는 가지 수))의 이전 정수
  - 실제로 순열에서 수를 빼서 만들기
"""
import math


# 1번 퀴즈 해결
def solve_one(numbers, idx, length, k, answer):
    # 수가 다 배정되었다면 종료
    if idx == N:
        return

    # 전체 가지 수
    total = 1
    for i in range(1, length + 1):
        total *= i
    # 이번 수가 가지게 될 경우의 수
    cnt = total // length
    # 이번 자리 수의 위치 구하기
    location = (k - 1) // cnt
    # 정답 수에 배정
    answer[idx] = numbers.pop(location)
    # k 갱신(바뀐 자리 수 위치 반영)
    k -= cnt * location
    # 다음 자리 수 구하기
    solve_one(numbers, idx + 1, length - 1, k, answer)


# 2번 퀴즈 해결
def solve_two(numbers, idx, length, answer):
    global k
    if idx == N:
        return
    # 전체 가지 수
    total = 1
    for i in range(1, length + 1):
        total *= i
    # 이번 수가 가지게 될 경우의 수
    cnt = total // length
    # 정답 순열의 수의 위치
    location = numbers.index(answer[idx])
    # 정답 수 제거
    numbers.pop(location)
    k += cnt * location
    # 다음 자리 수 구하기
    solve_two(numbers, idx + 1, length - 1, answer)


# 1부터 N까지의 수
N = int(input())
numbers = [number for number in range(1, N + 1)]
# 소문제
quiz = list(map(int, input().split()))

# 1이 주어질 때
if quiz[0] == 1:
    k = quiz[1]
    # 정답 순열
    answer = [0] * N
    solve_one(numbers,0, N, k, answer)
    print(*answer)
# 2가 주어질 때
else:
    answer = quiz[1:]
    k = 1
    solve_two(numbers, 0, N, answer)
    print(k)



