import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
stack = []
time = 0
score = 0
answer = 0
for _ in range(N):
    info = list(map(int, input().split()))

    if info[0]:
        if time == 0:
            score = info[1]
            time = info[2]
        else:
            stack.append((score, time))
            score = info[1]
            time = info[2]

    if time > 0:
        time -= 1
        if time == 0:
            answer += score
            if stack:
                score, time = stack.pop()

print(answer)