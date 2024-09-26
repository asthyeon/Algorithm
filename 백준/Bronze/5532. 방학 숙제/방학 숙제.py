import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

math = B / D
if math > (B // D):
    math = int(B / D) + 1
language = A / C
if language > (A // C):
    language = int(A / C) + 1

print(int(L - max(math, language)))