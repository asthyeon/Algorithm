import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

top = int(input())
middle = int(input())
down = int(input())
cola = int(input())
cider = int(input())

print(min(top, middle, down) + min(cola, cider) - 50)
