import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

answer = 0
people = 0
for _ in range(10):
    drop, ride = map(int, input().split())

    people += ride
    people -= drop
    answer = max(answer, people)

print(answer)