import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 문자열 교환 (1522)
1. a와 b로만 이루어진 문자열이 주어질 때, a를 모두 연속으로 만들기 위해 필요한 교환의 회수?
2. 문자열은 원형(처음과 끝이 인접)
3. 슬라이딩 윈도우
 - a 전체 개수 만큼의 윈도우 -> 윈도우에 포함되지 못한 a의 개수 = 교환 수
* 변수명 개선 및 코드 축약해보기
"""

string = input().rstrip()
length = len(string)

# 전체 a 개수
cnt_a = string.count('a')

# 현재 b 개수(교환회수) 및 최댓값
current = string[:cnt_a].count('b')
answer = current

# 슬라이딩 윈도우
end = cnt_a - 1
for start in range(1, length):
    # 지난 값이 b라면 교환 -1, 마지막 값이 b라면 교환 +1
    if string[start - 1] == 'b':
        current -= 1
    if string[(start + end) % length] == 'b':
        current += 1
    # 값 갱신
    answer = min(answer, current)

print(answer)