import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 매직 스타
 1. 1 ~ 12 숫자가 헥사그램으로 채워진 매직 스타
 2. 숫자 네 개로 이루어진 줄의 숫자를 모두 합하면 26
 3. 일부만 채워진 매직 스타가 주어졌을 때 수를 전부 다 채우기
[입력]
 1. 매직 스타의 모양이 주어짐
  - 'x': 수가 채워져 있지 않음
  - 'A' ~ 'L': 1 ~ 11 숫자
  - '.': 모양 갖추기
[출력]
 1. 만들 수 있는 방법 중 사전 순으로 가장 앞서는 방법 출력
 2. 모든 줄을 순서대로 붙여서 하나의 문자열로 만든 뒤, 사전 순으로 비교
"""

"""
@ 풀이
 1. 백트래킹
"""

# 알파벳 숫자 치환
alphabets = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
    'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
    'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
    # 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
}
# 숫자 알파벳 치환
numbers = {
    1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E',
    6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
    11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O',
    16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T',
    # 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'
}


# 백트래킹
def back_tracking(oneline, index):
    # 26이 안되는 줄이 있을 경우 백
    if index == 5:
        if sum(oneline[1:5]) != 26:
            return
    elif index == 8:
        if oneline[0] + oneline[2] + oneline[5] + oneline[7] != 26:
            return
    elif index == 11:
        if oneline[0] + oneline[3] + oneline[6] + oneline[10] != 26:
            return
        elif sum(oneline[7:11]) != 26:
            return
    elif index == 12:
        if oneline[1] + oneline[5] + oneline[8] + oneline[11] != 26:
            return
        elif oneline[4] + oneline[6] + oneline[9] + oneline[11] != 26:
            return
        else:
            star(oneline)

    # 숫자 1 ~ 20 넣기
    for num in range(1, 21):
        # 이미 값이 부여되어 있으면 인덱스 올리기
        if oneline[index] != 0:
            back_tracking(oneline, index + 1)
            return

        if num not in oneline:
            oneline[index] = num
            back_tracking(oneline, index + 1)
            oneline[index] = 0


# 별 만들기
def star(oneline):
    print(f'....{numbers[oneline[0]]}....')
    print(f'.{numbers[oneline[1]]}.{numbers[oneline[2]]}.{numbers[oneline[3]]}.{numbers[oneline[4]]}.')
    print(f'..{numbers[oneline[5]]}...{numbers[oneline[6]]}..')
    print(f'.{numbers[oneline[7]]}.{numbers[oneline[8]]}.{numbers[oneline[9]]}.{numbers[oneline[10]]}.')
    print(f'....{numbers[oneline[11]]}....')
    exit()


# 매직 스타 정보를 한 줄로 만들기
oneline = []
for i in range(5):
    # 사이의 '.' 제거
    line = input().rstrip()
    line = line.strip('.')
    if i == 2:
        oneline += line.split('...')
    else:
        oneline += line.split('.')

# 숫자 치환
for j in range(len(oneline)):
    if oneline[j] in alphabets:
        oneline[j] = alphabets[oneline[j]]

# x를 0으로 치환
for k in range(12):
    if oneline[k] == 'x':
        oneline[k] = 0

back_tracking(oneline, 0)