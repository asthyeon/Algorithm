import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

S, K, H = map(int, input().split())

universities = {S: 'Soongsil', K: 'Korea', H: 'Hanyang'}

if S + K + H >= 100:
    print('OK')
else:
    print(universities[min(S, K, H)])