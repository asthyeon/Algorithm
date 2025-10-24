import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
<문제>
# 단어 정렬 (1181)
1. 문자열 단어 정렬
2. 중복된 단어는 하나만 남기고 제거
<풀이>
1. set 이용 -> 중복 제거
2. lambda 이용 -> 1순위 글자수, 2순위 사전순 정렬
"""

N = int(input())
# set 이용
words = set()
for _ in range(N):
    word = input().strip()
    words.add(word)

# lambda 이용
answer = sorted(list(words), key=lambda x: (len(x), x))
for ans in answer:
    print(ans)
