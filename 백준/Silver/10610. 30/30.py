import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 30 (10610)
 1. 길거리에서 찾은 수에 포함된 숫자들을 섞어 30의 배수가 되는 가장 큰 수 만들기
[입력]
 1. N: 길거리에서 찾은 수
[출력]
 1. 30의 배수 만들기, 존재하지 않는다면 -1 출력
"""

"""
<풀이>
 1. 일단 풀어보기
 2. 30의 배수 -> 0을 포함한 3의 배수
 3. 3의 배수 -> 모든 자릿수의 합이 3의 배수
 4. 끝은 0이므로 내림차순으로 가장 큰 값 파악
"""

N = input().rstrip()

# 0 불포함
if '0' not in N:
    print(-1)
# 0 포함
else:
    # 3의 배수 판별
    three = 0
    for n in N:
        three += int(n)

    # 3의 배수라면 가장 큰 값 출력
    if three % 3 == 0:
        N = sorted(N, reverse=True)
        answer = ''
        for n in N:
            answer += n
        print(answer)
    # 3의 배수가 아님
    else:
        print(-1)