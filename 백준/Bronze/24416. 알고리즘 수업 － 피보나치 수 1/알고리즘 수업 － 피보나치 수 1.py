import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline


def fibonacci(n):
    f = [0] * (n + 1)
    f[1] = f[2] = 1
    cnt = 0
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
        cnt += 1
    return f[n], cnt


n = int(input())

print(*fibonacci(n))