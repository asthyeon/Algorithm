import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

col = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
r_col = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H'}
row = {'8': 0, '7': 1, '6': 2, '5': 3, '4': 4, '3': 5, '2': 6, '1': 7}
r_row = {0: '8', 1: '7', 2: '6', 3: '5', 4: '4', 5: '3', 6: '2', 7: '1'}
mover = {'R': (0, 1), 'L': (0, -1), 'B': (1, 0), 'T': (-1, 0),
         'RT': (-1, 1), 'LT': (-1, -1), 'RB': (1, 1), 'LB': (1, -1)}

king, stone, N = input().split()

kx, ky = row[king[1]], col[king[0]]
sx, sy = row[stone[1]], col[stone[0]]
for _ in range(int(N)):
    command = input().rstrip()

    dx, dy = mover[command]
    nkx, nky = kx + dx, ky + dy
    nsx, nsy = sx + dx, sy + dy

    if 0 <= nkx < 8 and 0 <= nky < 8:
        if nkx == sx and nky == sy:
            if 0 <= nsx < 8 and 0 <= nsy < 8:
                kx, ky = nkx, nky
                sx, sy = nsx, nsy
        else:
            kx, ky = nkx, nky

print(r_col[ky] + r_row[kx])
print(r_col[sy] + r_row[sx])