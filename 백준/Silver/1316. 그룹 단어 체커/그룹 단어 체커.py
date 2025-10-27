import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
<문제>
# 그룹 단어 체커 (1316)
1. 그룹 단어: 각 문자가 연속해서 나타나는 경우만을 말함
<풀이>
1. 구현 -> set 이용
"""

answer = 0
N = int(input())
for _ in range(N):
    word = input().rstrip()
    
    # 중복 체크용 set, 직전 단어 저장할 tmp, 조건 불충족시 순회 종료
    checker = set()
    tmp = ''
    flag = False
    for w in word:
        # 처음으로 알파벳을 만나는 경우
        if w not in checker:
            checker.add(w)
            tmp = w
        # 두 번째로 알파벳을 만나는 경우
        else:
            # 직전 단어라면 넘어가기
            if tmp == w:
                continue
            # 직전 단어가 아니라면 조건 불충족
            else:
                flag = True
                break
    # 조건 충족시 answer +1
    if not flag:
        answer += 1

print(answer)
