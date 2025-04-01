import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
words = [input().rstrip() for _ in range(N)]

# 단어 정렬
words.sort()
# 최대 크기
answer = N
for i in range(N):
    # 현재 단어보다 더 긴 단어 순회
    for j in range(i + 1, N):
        # 현재 단어가 접두사라면 크기 줄이기
        if words[i] == words[j][:len(words[i])]:
            answer -= 1
            break

print(answer)