import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 비밀번호 찾기 (17219)
 1. 비밀번호 찾기
[입력]
 1. N: 사이트 주소 수, M: 비밀번호를 찾으려는 사이트 주소 수
 2. N개의 줄: 각 줄에 사이트 주소와 비밀번호가 공백으로 주어짐
 3. M개의 줄: 비밀번호를 찾으려는 사이트 주소가 한 줄에 하나씩 입력됨
[출력]
 1. M개의 줄에 걸쳐 비밀번호를 찾으려는 사이트의 비밀번호를 차례대로 출력
"""

"""
<풀이>
 1. 자료구조
"""

saved = {}

N, M = map(int, input().split())
for _ in range(N):
    site, password = map(str, input().split())

    saved[site] = password

for _ in range(M):
    site = input().rstrip()

    print(saved[site])

