import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 중복 제거 (13701)
 1. N개의 정수를 읽고, 이들 중에서 반복되는 수를 제외하고 남은 N'개의 수를 입력된 순서대로 출력
[입력]
 1. 첫째 줄에 N개의 수가 주어짐 (0 <= Ai < 2**25)
[출력]
 1. N'개의 수 출력
"""

"""
<풀이>
 1. 세트 이용 -> 메모리 초과
 2. 비트마스킹: 하나의 숫자를 하나의 비트에 대응시켜 표현
"""

# 숫자를 비트로 저장할 수 있는 배열 생성
arr = bytearray(2**22)
# 각 숫자를 저장할 문자열
string = ''

# 입력을 1글자씩 읽기 위한 반복문
while True:
    # 한 글자씩 읽기
    one = sys.stdin.read(1)

    # 이 글자가 숫자라면 문자열에 이번 숫자를 저장
    if one.isnumeric():
        string += one

    # 이 글자가 숫자가 아니라면
    else:
        # 문자열을 숫자로 바꾸기
        number = int(string)

        # 숫자 number를 arr배열의 byte번째 바이트의 bite번째 비트에 저장
        # 숫자를 8로 나눠 바이트로 저장
        byte = number // 8
        # 숫자를 8로 나눈 후 나머지를 비트로 저장
        bit = number % 8

        # 해당 숫자가 배열에 저장되어 있는지 확인
        if not arr[byte] & (1 << bit):
            # 저장되어 있다면 출력
            print(number, end=' ')
            # 비트 OR 할당 연산자를 통해 배열에 저장
            arr[byte] |= 1 << bit

        # 문자열 초기화
        string = ''
        
        # 공백이 아니라면 반복문 종료
        if one != ' ':
            break
