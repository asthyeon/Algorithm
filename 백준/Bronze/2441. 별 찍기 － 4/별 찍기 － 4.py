import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

for i in range(N):
    space = ' ' * i
    star = '*' * (N - i)
    
    print(space + star)