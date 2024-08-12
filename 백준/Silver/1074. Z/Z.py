import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def dfs(r, c, size, order):
    size = size // 2

    if r < size and c < size:
        if size == 1:
            print(order)
            exit()

        dfs(r, c, size, order)

    elif r < size and c >= size:
        if size == 1:
            print(order + 1)
            exit()

        dfs(r, c - size, size, order + size ** 2)

    elif r >= size and c < size:
        if size == 1:
            print(order + 2)
            exit()

        dfs(r - size, c, size, order + size ** 2 * 2)

    elif r >= size and c >= size:
        if size == 1:
            print(order + 3)
            exit()

        dfs(r - size, c - size, size, order + size ** 2 * 3)


N, r, c = map(int,input().split())

dfs(r, c, 2 ** N, 0)