import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

M = int(input())
N = int(input())

prime_numbers = []
for number in range(M, N + 1):
    if number >= 2:
        prime = True
        for i in range(2, number):
            if number % i == 0:
                prime = False
                break
        if prime:
            prime_numbers.append(number)

if prime_numbers:
    print(sum(prime_numbers))
    print(prime_numbers[0])
else:
    print(-1)


