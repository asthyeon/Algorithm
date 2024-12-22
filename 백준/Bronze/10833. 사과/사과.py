import sys
input = sys.stdin.readline

N = int(input())

answer = 0
for _ in range(N):
    students, apples = map(int, input().split())
    
    answer += apples - ((apples // students) * students)

print(answer)