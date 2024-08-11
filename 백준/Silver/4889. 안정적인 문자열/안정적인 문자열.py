import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 안정적인 문자열 (4889)
 1. 안정적인 문자열
  ㄱ. 빈 문자열은 안정적
  ㄴ. S가 안정적이라면 {S}도 안정적
  ㄷ. S와 T가 안정적이라면 ST(두 문자열의 연결)도 안정적
 2. 가능한 연산은 여는 괄호를 닫는 괄호로 바꾸거나, 닫는 괄호를 여는 괄호로 바꾸는 것
[입력]
 1. 입력의 마지막 줄은 '-'가 한 개 이상 주어짐
[출력]
 1. 각 테스트 케이스에 대해서 필요한 최소 연산의 수 출력
"""

"""
<풀이>
 1. 스택
"""

# 문제 번호
number = 1
while True:
    string = input().rstrip()

    # 종료 조건
    if '-' in string:
        break

    # 스택, 연산 수
    stack = []
    cnt = 0

    for s in string:
        # 여는 괄호면 인스택
        if s == '{':
            stack.append('{')
        # 닫는 괄호이고 스택이 있으면 제거 (연산 X)
        elif s == '}' and stack:
            stack.pop()
        # 닫는 괄호이고, 스택이 차있지 않으면 연산 +1
        else:
            cnt += 1
            stack.append('{')
            
    # 남은 스택의 1/2 만큼 연산
    cnt += len(stack) // 2
    # 출력
    print(f'{number}. {cnt}')
    number += 1