import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
1 1
2 3
3 5
4 7
"""

N = int(input())
mark = '*'
space = N
star = 0
for i in range((N * 2) - 1):
    if i <= N - 1:
        space -= 1
        star += 1
    else:
        space += 1
        star -= 1
    print(' ' * space + mark * star)