import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

total = A + B + C

if A == B == C == 60:
    print('Equilateral')
elif total == 180:
    if A == B or B == C or C == A:
        print('Isosceles')
    elif A != B and B != C and C != A:
        print('Scalene')
elif total != 180:
    print('Error')