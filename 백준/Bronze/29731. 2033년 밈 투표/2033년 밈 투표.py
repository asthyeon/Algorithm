import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

promises = set()
promises.add('Never gonna give you up')
promises.add('Never gonna let you down')
promises.add('Never gonna run around and desert you')
promises.add('Never gonna make you cry')
promises.add('Never gonna say goodbye')
promises.add('Never gonna tell a lie and hurt you')
promises.add('Never gonna stop')

N = int(input())
for _ in range(N):
    promise = input().rstrip()

    if promise not in promises:
        print('Yes')
        exit()
print('No')