import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    number = int(input())
    changed = bin(number)

    answer = []
    cnt = 0
    for i in range(len(changed) - 1, -1, -1):
        if changed[i] == '1':
            answer.append(cnt)
        cnt += 1

    print(*answer)