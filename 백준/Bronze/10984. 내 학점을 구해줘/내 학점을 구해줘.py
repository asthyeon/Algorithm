import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    subjects = 0
    grade = 0
    for _ in range(N):
        C, G = map(float, input().split())

        subjects += C
        grade += C * G

    print(int(subjects), round(grade / subjects, 1))