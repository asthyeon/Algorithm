import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 포스택 (25556)
 1. 길이가 N인 순열 A와 네 개의 비어 있는 스택
 2. 순열을 청소하는 것: 다음 과정을 통해 순열을 오름차순으로 정렬하는 것
  ㄱ. A의 원소들을 앞 원소부터 순서대로 네개의 스택 중 하나에 삽입
  ㄴ. A의 모든 원소를 스택에 삽입했다면, 원하는 스택에서 꺼내는 것 반복하여 모든 수 꺼내기
  ㄷ. 꺼낸 수들을 순서대로 오른쪽에서 왼쪽으로 나열(가장 처음에 꺼낸 수가 맨 뒤)
[입력]
 1. N: 순열의 길이
 2. 순열 A의 원소
[출력]
 1. 순열 청소 가능시 YES, 불가능하다면 NO 출력
"""

"""
<풀이>
 1. 스택
"""

N = int(input())
A = list(map(int, input().split()))

# 네 개의 스택
stack1 = []
stack2 = []
stack3 = []
stack4 = []

previous = False
# 스택 쌓기
for a in A:
    # 스택이 비어있는 경우 삽입, 차있는 경우 오름차순일 경우 삽입
    if not stack1:
        stack1.append(a)
    elif a > stack1[-1]:
        stack1.append(a)
    elif not stack2:
        stack2.append(a)
    elif a > stack2[-1]:
        stack2.append(a)
    elif not stack3:
        stack3.append(a)
    elif a > stack3[-1]:
        stack3.append(a)
    elif not stack4:
        stack4.append(a)
    elif a > stack4[-1]:
        stack4.append(a)
    # 어느 스택에도 들어가지 못하는 경우 순열 청소 불가
    else:
        print('NO')
        break
# 모든 수가 들어갔다면 순열 청소 가능
else:
    print('YES')