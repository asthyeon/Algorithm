import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

to_s = int(input())
to_p = int(input())
to_a = int(input())
to_h = int(input())

total = to_s + to_p + to_a + to_h

x = total // 60
y = total % 60

print(x)
print(y)

