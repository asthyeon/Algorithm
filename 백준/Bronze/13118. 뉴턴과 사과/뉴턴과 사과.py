import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

p1, p2, p3, p4 = map(int, input().split())
x, y, r = map(int, input().split())

if x == p1:
    print(1)
elif x == p2:
    print(2)
elif x == p3:
    print(3)
elif x == p4:
    print(4)
else:
    print(0)