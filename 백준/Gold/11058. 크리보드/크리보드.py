import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 크리보드 (11058)
 1. 크리보드 버튼
  ㄱ. 화면에 A 출력
  ㄴ. Ctrl-A: 화면을 전체 선택
  ㄷ. Ctrl-C: 전체 선택한 내용을 버퍼에 복사
  ㄹ. Ctrl-V: 버퍼가 비어있지 않은 경우, 화면에 출력된 문자열의 바로 뒤에 버퍼의 내용 붙여넣기
[입력]
 1. N: 버튼을 누르는 횟수
[출력]
 1. 버튼을 총 N번 눌러서 화면에 출력할 수 있는 A 개수의 최댓값 출력
"""

"""
<풀이>
 1. dp
 2. 버튼 ㄹ을 입력하기 위해서 ㄴ - ㄷ - ㄹ 총 3번 필요 
N = 1: ㄱ: A
N = 2: ㄱ - ㄱ: AA
N = 3: ㄱ - ㄱ - ㄱ: AAA
N = 4: ㄱ - ㄱ - ㄱ - ㄱ: AAAA
N = 5: ㄱ - ㄱ - ㄱ - ㄱ - ㄱ: AAAAA
N = 6: ㄱ - ㄱ - ㄱ - ㄴ - ㄷ - ㄹ = ㄱ - ㄱ - ㄱ - ㄱ - ㄱ - ㄱ: AAAAAA
(복붙 2배)
N = 7: ㄱ - ㄱ - ㄱ - ㄴ - ㄷ - ㄹ - ㄹ: AAAAAAAAA
(복붙 3배)
N = 8: ㄱ - ㄱ - ㄱ - ㄴ - ㄷ - ㄹ - ㄹ - ㄹ: AAAAAAAAAAAA
(복붙 4배)
N = 9: ㄱ - ㄱ - ㄱ - ㄱ - ㄴ - ㄷ - ㄹ - ㄹ - ㄹ: A 16개
(복붙은 3번이 최대)
 2. 버퍼에 들어가 있는 A의 개수가 N개만 출력하는 것보다 많아질 수 있을 때
"""


# dp
def dynamic_programming(N):
    # 기본 값은 A를 출력하는 버튼을 누를 때
    dp = [i for i in range(N + 1)]

    # 7부터 버퍼를 이용
    for j in range(7, N + 1):
                    # 3개 이전의 2배
        dp[j] = max(dp[j - 3] * 2,
                    # 4개 이전의 3배
                    dp[j - 4] * 3,
                    # 5개 이전의 4배
                    dp[j - 5] * 4)

    return dp[N]


N = int(input())

print(dynamic_programming(N))