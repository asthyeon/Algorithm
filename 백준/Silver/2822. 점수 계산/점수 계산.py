import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

scores = []
numbering = {}
for i in range(1, 9):
    score = int(input())
    scores.append(score)
    numbering[score] = i

scores.sort()
numbers = []
for j in range(3, 8):
    numbers.append(numbering[scores[j]])
numbers.sort()

print(sum(scores[3:]))
print(*numbers)
