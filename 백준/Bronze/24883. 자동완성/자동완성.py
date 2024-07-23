import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

alphabet = input().rstrip()

if alphabet == 'N' or alphabet == 'n':
    print('Naver D2')
else:
    print('Naver Whale')