import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
print(int(N * 0.78), int(N - N * 0.2 * 0.22))