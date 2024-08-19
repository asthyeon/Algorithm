import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    n = int(input())

    clothes = {}
    for i in range(n):
        cloth, part = map(str, input().split())

        if part not in clothes:
            clothes[part] = []
        clothes[part].append(cloth)

    cnt = 1
    for cloth in clothes:
        cnt *= (len(clothes[cloth]) + 1)
    
    print(cnt - 1)