import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
no = 0
yes = 0
for _ in range(N):
    vote = int(input())
    
    if vote == 0:
        no += 1
    else:
        yes += 1

if no > yes:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')