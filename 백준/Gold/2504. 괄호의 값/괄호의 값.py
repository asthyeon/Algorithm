import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 괄호의 값 (2504)
 1. 올바른 괄호열
  - 한 쌍의 괄호로만 이루어진 '()', '[]'
  - 만일 x가 올바른 괄호열이면, '(x)', '[x]'도 모두 올바른 괄호열
  - x와 y 모두 올바른 괄호열이면, xy도 올바른 괄호열
 2. 각 괄호열의 값
  - '()' = 2
  - '[]' = 3
  - '(x)' = 2 * x
  - '[x]' = 3 * x
  - xy = x + y
[입력]
 1. 괄호열
[출력]
 1. 그 괄호열의 값을 나타내는 정수 출력
"""

"""
<풀이>
 1. 스택
"""


def calculator(string):
    # 스택, 정답, 곱셈을 저장할 수
    stack = []
    answer = 0
    tmp = 1

    # 괄호열 계산
    for i in range(len(string)):

        # 소괄호일 때
        if string[i] == '(':
            stack.append(string[i])
            tmp *= 2
        # 닫힌 괄호를 만났을 때는 마지막 스택 제거 및 곱셈 정상화
        elif string[i] == ')':
            # 짝이 맞지 않는 경우 종료
            if not stack or stack[-1] == '[':
                return 0
            # 이번이 제일 내부의 값이라면 answer 에 값 더하기
            if string[i - 1] == '(':
                answer += tmp
            # 스택 제거 및 곱셈 정상화
            stack.pop()
            tmp //= 2

        # 대괄호일 때
        elif string[i] == '[':
            stack.append(string[i])
            tmp *= 3
        else:
            # 짝이 맞지 않는 경우 종료
            if not stack or stack[-1] == '(':
                return 0
            # 이번이 제일 내부의 값이라면 answer 에 값 더하기
            if string[i - 1] == '[':
                answer += tmp
            # 스택 제거 및 곱셈 정상화
            stack.pop()
            tmp //= 3
    
    # 스택이 비어 있어야 정답 출력
    if not stack:
        return answer
    else:
        return 0


string = input().rstrip()

print(calculator(string))