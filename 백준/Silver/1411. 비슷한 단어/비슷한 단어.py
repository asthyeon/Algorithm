import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 비슷한 단어(1411)
 1. 어떤 단어 A를 숌스럽게 바꿔서 또다른 단어 B로 만든다면, 그 단어는 비슷한 단어
 2. 숌스럽게 바꾼다
  - 단어 A에 등장하는 모든 알파벳을 다른 알파벳으로 바꾸는 것
  - 단어에 등장하는 알파벳의 순서는 바뀌지 않음
  - 두 개의 다른 알파벳을 하나의 알파벳으로 바꿀 수 없음
  - 임의의 알파벳을 자기 자신으로 바꾸는 것은 가능
 3. 단어가 여러 개 주어졌을 때, 몇 개의 쌍이 비슷한지 구하기
[입력]
 1. N: 단어의 개수
 2. ~ N개의 줄: 한 줄에 하나씩 단어가 주어짐
 3. 모든 단어의 길이는 같고, 중복되지 않음
[출력]
 1. 총 몇 개의 쌍이 비슷한지 출력
"""

"""
<풀이>
 1. 한 단어와 모든 단어를 매치해보기
 2. 기준 단어에서 사용된 알파벳은 딕셔너리로 중복처리
 3. 리스트를 이용하여 인덱스별로 중복된 단어가 사용되면 +1
"""

# 단어의 개수 N
N = int(input())

# 단어 입력
words = []
for _ in range(N):
    word = input().rstrip()
    words.append(word)

# 단어 길이
length = len(words[0])

# 각 단어 비교
indexes = []
for standard in range(N):
    # 중복처리용 딕셔너리
    duple = {}
    # 인덱스 값
    idx = [0] * length
    # 기준 단어 분석
    for i in range(length):
        # 중복이 아니라면 1
        if words[standard][i] not in duple:
            duple[words[standard][i]] = 1
        # 중복이라면 +1
        else:
            duple[words[standard][i]] += 1
        # 인덱스 값 할당
        idx[i] = duple[words[standard][i]]

    # 단어들을 정수형으로 바꾼 리스트
    indexes.append(idx)

# 비슷한 단어의 개수
cnt = 0
# 기준 단어와 다른 단어를 모두 비교
for standard in range(N - 1):
    for comparison in range(standard + 1, N):
        # 형태가 같다면 각 알파벳이 모두 다른지 확인하기
        if indexes[standard] == indexes[comparison]:
            # 비교 위치의 알파벳 비교
            alphabets = {}
            for j in range(length):
                # 인덱스 값이 1일 때(알파벳이 처음 쓰일 때)는 딕셔너리에 추가
                if indexes[standard][j] == 1:
                    alphabets[words[standard][j]] = words[comparison][j]
                # 인덱스 값이 2이상일 때(알파벳이 여러번 쓰일 때)
                else:
                    # 이번 위치의 알파벳이 다른 알파벳으로 쓰인 거라면 종료하기
                    if alphabets[words[standard][j]] != words[comparison][j]:
                        break
            # 문제가 없다면 비슷한 단어의 개수 +1
            else:
                cnt += 1
                
print(cnt)











