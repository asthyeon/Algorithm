import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 애너그램 (6443)
 1. 입력받은 영단어의 철자들로 만들 수 있는 모든 단어 출력
 2. 중복된 철자로 같은 단어가 만들어질 수 있는데 한 번만 출력해야 함
 3. 알파벳 순서로 출력해야 함
[입력]
 1. N: 단어의 개수
 2. N개의 줄: 영단어
[출력]
 1. 알파벳 순서로 중복되지 않게 출력
"""

"""
<풀이>
 1. 조합 -> 메모리 초과
 2. 백트래킹 -> 브루트포스는 불가
 3. 단어를 형성하면서 그 단어로 시작되는 경우를 제외해야 함
"""


# 백트래킹
def back_tracking(word, new_word, used):
    # 단어 형성
    if len(new_word) == len(word):
        if new_word not in anagram:
            anagram.add(new_word)
        return

    # 사용되지 않은 알파벳만 사용
    for i in range(len(word)):
        # 사용된 시작 단어들도 기록하기
        if i not in used and new_word + word[i] not in using:
            using.add(new_word + word[i])
            back_tracking(word, new_word + word[i], used + [i])


N = int(input())
for _ in range(N):
    word = input().rstrip()

    using = set()
    anagram = set()
    # 백트래킹 (원래 단어, 새로운 단어, 사용된 알파벳 리스트)
    back_tracking(word, '', [])

    # 정렬 후 출력
    new_anagram = sorted(list(anagram))
    for new in new_anagram:
        print(new)