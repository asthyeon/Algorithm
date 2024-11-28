import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 램프 (1034)
 1. 모든 램프는 켜져있거나 꺼져있다
 2. 스위치를 누를 때마다 그 열에 있는 램프의 상태가 바뀜
 3. 스위치를 K번 누르는데, 서로다른 스위치 K개를 누르지 않아도 됨
 4. 행이 켜져있다: 어떤 행에 있는 램프가 모두 켜져있을 때
[입력]
 1. N: 행의 개수, M: 열의 개수
 2. N개의 줄: 램프의 상태(1: 켜져있는 상태, 0: 꺼져있는 상태)
 3. K: 스위치를 누르는 횟수
[출력]
 1. 스위치를 K번 누른 후에 켜져있는 행의 최댓값 구하기
"""

"""
<풀이>
 1. 0의 개수가 K보다 크면 켜질 수 없음
 2. 같은 행은 같은 조건
"""

N, M = map(int, input().split())
lamps = [list(input().rstrip()) for _ in range(N)]
K = int(input())

# 각 행 중복 제거 및 켜질 수 있는 행 수
light = {}
for lamp in lamps:
    # 문자화 및 중복 체크
    string = ''.join(lamp)
    if string not in light:
        light[string] = 0

    # 0 개수 세기
    cnt = string.count('0')

    # 0이 K개보다 작거나 같고, 스위치 조작으로 모두 켤 수 있을 때
    if cnt <= K and (K - cnt) % 2 == 0:
        # 켜질 수 있는 행 수 증가
        light[string] += 1

# 가장 큰 값 출력
print(max(light.values()))



