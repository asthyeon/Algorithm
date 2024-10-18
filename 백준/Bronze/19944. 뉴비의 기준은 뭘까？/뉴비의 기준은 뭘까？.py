import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
if M <= 2:
    print('NEWBIE!')
elif M <= N:
    print('OLDBIE!')
else:
    print('TLE!')