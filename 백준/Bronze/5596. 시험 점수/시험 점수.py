import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

I1, M1, S1, E1 = map(int, input().split())
I2, M2, S2, E2 = map(int, input().split())

S = I1 + M1 + S1 + E1
T = I2 + M2 + S2 + E2

print(max(S, T))