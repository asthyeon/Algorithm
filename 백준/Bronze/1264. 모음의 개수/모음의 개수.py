import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

while True:
    sentence = input().rstrip()

    if sentence == '#':
        break

    cnt = 0
    for alphabet in sentence:
        if alphabet in vowels:
            cnt += 1

    print(cnt)