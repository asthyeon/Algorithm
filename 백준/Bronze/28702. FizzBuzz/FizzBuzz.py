import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline


def printer(answer):
    if answer % 3 == 0 and answer % 5 == 0:
        return 'FizzBuzz'
    elif answer % 3 == 0:
        return 'Fizz'
    elif answer % 5 == 0:
        return 'Buzz'
    else:
        return answer


words = {'FizzBuzz', 'Fizz', 'Buzz'}
w1 = input().rstrip()
w2 = input().rstrip()
w3 = input().rstrip()

if w1 not in words:
    answer = int(w1) + 3
elif w2 not in words:
    answer = int(w2) + 2
else:
    answer = int(w3) + 1

print(printer(answer))