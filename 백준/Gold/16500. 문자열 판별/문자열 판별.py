import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 문자열 판별 (16500)
 1. 문자열 S와 단어 목록 A가 주어졌을 때
 2. S를 A에 포함된 문자열을 한 개 이상 공백 없이 붙여서 만들 수 있는지 없는지
[입력]
 1. S: 문자열
 2. N: A에 포함된 문자열 수
 3. N개의 줄: A에 포함된 단어
[출력]
 1. A에 포함된 문자열로 S를 만들 수 있으면 1, 없으면 0 출력
"""

"""
<풀이>
 1. dp
"""


# dp
def dynamic_programming(words):
    dp = [0] * (len(S) + 1)
    # 시작점 설정
    dp[0] = 1

    # S + 1의 길이만큼 순회
    for i in range(len(S) + 1):
        # 단어 순회
        for word in words:
            # print(f'i: {i}')
            # print(f'S: {S[i - len(word):i]}')
            # print(f'word: {word}')
            # 이번 순서가 비교할 단어의 길이와 같거나 길고, 단어가 성립이 될 때
            if i >= len(word) and dp[i - len(word)] == 1:
                # 이번 부분이 비교할 단어와 같다면 dp값 1로 설정
                if S[i - len(word):i] == word:
                    dp[i] = 1
    
    # 마지막 값 출력
    return dp[len(S)]


S = input().rstrip()
N = int(input())
# 단어 리스트
words = []
for _ in range(N):
    word = input().rstrip()
    words.append(word)

print(dynamic_programming(words))