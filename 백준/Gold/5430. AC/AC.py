import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# AC (5430)
 1. 함수 R: 배열에 있는 수의 순서를 뒤집음
 2. 함수 D: 첫 번째 수를 버림
 3. 함수는 조합해서 한 번에 사용 가능
[입력]
 1. T: 테스트 케이스의 개수
 2. p: 수행할 함수
 3. n: 배열에 들어 있는 수의 개수
 4. x: 배열에 들어있는 정수들
[출력]
 1. 주어진 정수 배열에 함수를 수행한 결과 출력
  (에러가 발생한 경우에는 error를 출력)
"""

"""
<풀이>
 1. 문자열 -> 정수만 남긴 배열 -> 시간초과
 2. 문자열 파싱 -> 시간초과
 3. 덱 사용 -> 시간초과
 4. 뒤집기를 간소화하기
"""
from collections import deque


T = int(input())
for tc in range(1, T + 1):
    p = input().rstrip()
    n = int(input())
    x = input().rstrip()

    # 덱에 정수로 넣기
    d = deque([])
    tmp = ''
    for i in x:
        if i == '[':
            continue
        elif i == ']':
            if tmp:
                d.append(int(tmp))
        elif i == ',':
            d.append(int(tmp))
            tmp = ''
        else:
            tmp += i

    # 함수 적용
    reverse = 0
    for function in p:
        if function == 'R':
            reverse += 1
        else:
            # 수가 존재할 때
            if d:
                # 뒤바꿔야 한다면 맨 뒤를 제거
                if reverse % 2 == 1:
                    d.pop()
                # 뒤바뀌지 않으면 맨 앞을 제거
                else:
                    d.popleft()
            # 수가 존재 하지 않으면 종료
            else:
                d = 'error'
                break

    # 조건에 따라 출력
    if d == 'error':
        print(d)
    else:
        answer = '['
        # 뒤집어야 하는 경우
        if reverse % 2 == 1:
            while d:
                answer += str(d.pop())
                if d:
                    answer += ','
            answer += ']'
        # 뒤집지 않는 경우
        else:
            while d:
                answer += str(d.popleft())
                if d:
                    answer += ','
            answer += ']'

        print(answer)