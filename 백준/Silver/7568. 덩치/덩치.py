import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
people = []
for _ in range(N):
    w, h = map(int, input().split())
    people.append((w, h))

ranked = [1] * N
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            ranked[i] += 1

print(*ranked)