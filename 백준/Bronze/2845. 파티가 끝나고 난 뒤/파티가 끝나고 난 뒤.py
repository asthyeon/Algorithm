import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

L, P = map(int, input().split())
participants = list(map(int, input().split()))

original = L * P
for participant in participants:
    print(participant - original, end=' ')