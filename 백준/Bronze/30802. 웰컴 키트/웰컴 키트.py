import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

shirts = 0

for i in range(6):
    if (sizes[i] / T) > (sizes[i] // T):
        shirts += (sizes[i] // T + 1)
    else:
        shirts += (sizes[i] // T)

print(shirts)
print(N // P, N % P)