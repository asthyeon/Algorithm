import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N, A, B = map(int, input().split())
if B > A:
    print('Bus')
elif B < A:
    print('Subway')
else:
    print('Anything')