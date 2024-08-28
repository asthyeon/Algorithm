import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

letter = input().rstrip()

if letter == 'M':
    print('MatKor')
elif letter == 'W':
    print('WiCys')
elif letter == 'C':
    print('CyKor')
elif letter == 'A':
    print('AlKor')
else:
    print('$clear')