import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 문자열게임 2
1. 게임의 진행 방식(T회 반복)
 [1] 알파벳 소문자로 이루어진 문자열 W가 주어짐
 [2] 양의 정수 K가 주어짐
 [3] 어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이 구하기
 [4] 어떤 문자를 정확히 K개를 포함하고, 문자열의 처음과 마지막이 해당 문자로,
     가장 긴 연속 문자열의 길이 구하기
* 입력
- 첫째 줄: 게임의 수 T
- 다음 줄 ~ 2개의 줄: 문자열 W, 정수 K
[출력: T개의 줄 동안 문자열 게임의 3번과 4번에서 구한 연속 문자열의 길이 출력,
       만족하는 연속 문자열이 없을 시 -1 출력]
"""

"""
@ 풀이
(1) 그냥 풀어보기
"""

# 문자열 게임의 수
T = int(input())
for tc in range(T):
    # 문자열
    word = input().rstrip()
    # 문자열에서 포함해야할 조건의 길이 K
    K = int(input())

    # 알파벳 딕셔너리
    alphabets = {}
    for w in word:
        if w not in alphabets:
            alphabets[w] = 1
        else:
            alphabets[w] += 1

    # 딕셔너리에서 K개를 만족하는 알파벳 찾기
    candidates = []
    for alphabet in alphabets:
        if alphabets[alphabet] >= K:
            candidates.append(alphabet)

    # 조건을 만족하는 알파벳이 없다면 넘기기
    if not candidates:
        print(-1)
        continue

    # 3번 조건 만족하는 문자열 길이
    short = 10e9
    # 4번 조건 만족하는 문자열 길이
    long = 0
    # 후보가 될 수 있는 알파벳 순회
    for candidate in candidates:
        # 나온 횟수
        cnt = 0
        # 문자열의 길이를 세기 위한 리스트
        start = []
        # 문자열 리스트 인덱스 번호
        start_number = 0
        # 문자열 길이
        size = len(word)
        # 이번 문자열의 길이
        length = 0
        # 문자열 길이만큼 반복
        for i in range(size):
            # 이번 알파벳이 후보라면 횟수 + 1, 리스트에 넣기
            if word[i] == candidate:
                cnt += 1
                start.append(i)
            # 문자열 횟수가 K번이 되었다면
            if cnt == K:
                # 문자열 길이 재기
                length = i - start[start_number] + 1
                # 3번 조건 체크
                short = min(short, length)
                # 4번 조건 체크
                long = max(long, length)
                # 딕셔너리 감소 시키기
                alphabets[candidate] -= 1
                # 남은 문자열이 K보다 작다면 넘기기
                if alphabets[candidate] < K:
                    break
                # 횟수를 -1 해서 남은 문자열에서도 조건을 만족하는지 확인
                cnt -= 1
                # 스타트 지점을 변경하기 위해 인덱스 +1
                start_number += 1

    print(short, long)

