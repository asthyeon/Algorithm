import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

while True:
    n = int(input())

    if n == -1:
        break

    divisors = []
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            divisors.append(i)

    if sum(divisors) == n:
        print(f'{n} = {divisors[0]}', end='')
        for divisor in range(1, len(divisors)):
            print(f' + {divisors[divisor]}', end='')
        print()
    else:
        print(f'{n} is NOT perfect.')