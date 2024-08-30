import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

N %= 14
print('WelcomeToSMUPC'[N - 1])