import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

# 한글의 유니코드 시작 번호 = 44032
start_korean = 44031
change_korean = chr(start_korean + N)

print(change_korean)