import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 수 이어 쓰기 2 (1790)
 1. 1부터 N까지의 수를 이어서 씀
 2. 앞에서 k번째 자리 숫자가 어떤 숫자인지 구하기
[입력]
 1. N, k
[출력]
 1. k번째 자리 숫자 출력, 수의 길이가 k보다 작아서 k번째 자리 숫자가 없는 경우는 -1 출력
"""

"""
<풀이>
 1. 
- 1의 자리: 1 ~ 9 [9개]
- 2의 자리: 10 ~ 99 [90개]
- 3의 자리: 100 ~ 999 [900개]
"""

N, k = map(int, input().split())

# 현재 자릿수와 그 수의 개수, 마지막 수
digit = 1
digit_cnt = 9
last = 0

# 남은 자릿수가 현재 자릿수의 개수보다 크다면
while k > digit * digit_cnt:

    # k 값 및 마지막 수 조정
    k -= digit * digit_cnt
    last += digit_cnt

    # 자릿수 이동
    digit += 1
    digit_cnt *= 10

# k번째 자리에 사용되는 숫자 찾기 (자릿수 맞추기) + (현재 수가 몇 번째 인지 조정)
number = (last + 1) + ((k - 1) // digit)

# k번째 자리에 사용되는 숫자가 N보다 작거나 같다면
if number <= N:
    # k번째 자리 숫자 출력
    print(str(number)[(k - 1) % digit])
# k번째 자리 숫자가 없는 경우 -1 출력
else:
    print(-1)