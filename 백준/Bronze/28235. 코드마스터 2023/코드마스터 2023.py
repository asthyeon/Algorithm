import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

crying = input().rstrip()
if crying == 'SONGDO':
    print('HIGHSCHOOL')
elif crying == 'CODE':
    print('MASTER')
elif crying == '2023':
    print('0611')
else:
    print('CONTEST')