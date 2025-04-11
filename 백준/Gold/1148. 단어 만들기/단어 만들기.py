import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 단어 만들기 (1148)
 1. 영문자들을 사용해서 최대한 많은 영단어 만들기
 2. 단어는 최소 4글자 이상, 한 글자당 최대 1번만 사용 가능, 정중앙 글자는 반드시 사용
[입력]
 1. 최대 20만 개의 단어가 주어짐, 입력의 끝에는 '-'
 2. 여러 개의 퍼즐판이 주어짐, 입력의 끝에는 '#'
[출력]
 1. 각 퍼즐판마다 정답 수가 가장 적은 정중앙 문자와 수, 반대의 경우 출력
   (한 개 이상의 문자가 답을 만족할 경우 문자들을 알파벳순으로 정렬하여 출력, 중복 출력 X)
"""

"""
<풀이> 
 1. 구현 
 2. 각 단어가 사전에 중복으로 존재할 수 있음 -> 사전을 set가 아닌 dict로 저장 
 3. 단어가 가능한 최대 수는 20만개
"""
from itertools import permutations

# 사전 형성
dictionary = {}
while True:
    word = input().rstrip()
    if word == '-':
        break
    if word not in dictionary:
        dictionary[word] = 0
    dictionary[word] += 1

# 퍼즐 형성
while True:
    puzzle = input().rstrip()
    if puzzle == '#':
        break

    # 각 알파벳의 사용 수
    alphabets = {}
    for p in set(puzzle):
        alphabets[p] = 0

    # 만들 수 있는 문자열 조사
    used = set()
    for r in range(4, 10):
        for string in list(permutations(puzzle, r)):
            string = ''.join(string)
            # 사전에 있는 단어라면, 사용 후 각 글자가 사용된 수 증가
            if string in dictionary:
                if string not in used:
                    used.add(string)
                    # 중복된 단어의 수만큼 증가
                    for s in set(string):
                        alphabets[s] += dictionary[string]

    # 정답 구하기
    minimum = 200000
    min_answer = []
    maximum = 0
    max_answer = []
    # 각 알파벳별
    for a in alphabets:
        # 가장 적게 사용된 알파벳
        if alphabets[a] < minimum:
            minimum = alphabets[a]
            min_answer = [a]
        elif alphabets[a] == minimum:
            min_answer.append(a)
        # 가장 많이 사용된 알파벳
        if alphabets[a] > maximum:
            maximum = alphabets[a]
            max_answer = [a]
        elif alphabets[a] == maximum:
            max_answer.append(a)

    # 정답 출력(알파벳은 사전순)
    print(''.join(sorted(min_answer)), minimum, ''.join(sorted(max_answer)), maximum)

