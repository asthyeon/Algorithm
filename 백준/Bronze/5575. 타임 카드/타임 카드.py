import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline


def timer(time):
    s = time[5] - time[2]
    if s < 0:
        s = 60 + s
        m = time[4] - time[1] - 1
    else:
        m = time[4] - time[1]
    if m < 0:
        m = 60 + m
        h = time[3] - time[0] - 1
    else:
        h = time[3] - time[0]

    return h, m, s


A_time = list(map(int, input().split()))
B_time = list(map(int, input().split()))
C_time = list(map(int, input().split()))

print(*timer(A_time))
print(*timer(B_time))
print(*timer(C_time))