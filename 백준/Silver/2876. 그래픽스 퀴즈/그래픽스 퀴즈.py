import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 그래픽스 퀴즈(2876)
 0. 교실 안에 N개의 책상이 한 줄로 늘어서 있고, 각 책상당 두 명이 앉아 있음
 1. 교수님은 학생들의 얼굴만 보고도 받아야 할 그레이드를 정확히 알아낼 수 있음
 2. 각 그레이드를 다른 색으로 표시
 3. 수업 방식
  - 교수님이 수업이 시작할 때 어떤 두 책상 선택
  - 두 책상과 그 사이에 있는 모든 책상에서 각각 한 명씩 지목해서 질문
  - 학생의 대답을 들음
 4. 바쁜 교수님은 한 가지 색 연필만 챙김
 5. 퀴즈에서 지목한 모두에게 같은 그레이드를 주려고 함
 6. 교수님이 채점할 수 있는 학생의 수는 최대 몇 명?
[입력]
 1. N: 책상 수
 2. N개의 줄: i번째 책상에 앉은 두 학생이 받아야 할 그레이드 A와 B가 주어짐
[출력]
 1. 교수님이 한 가지 색만을 이용해 채점할 수 있는 최대 학생 수와 그 때 그레이드 출력
 2. 답이 여러 가지라면, 가장 작은 그레이드 출력
"""

"""
<풀이>
 1. 딕셔너리 이용
"""

# 책상 수 N
N = int(input())
# 연속성 체크를 위한 수
grades = {
    1: 0, 2: 0, 3: 0, 4: 0, 5: 0
}
continues = {
    1: False, 2: False, 3: False, 4: False, 5: False
}
# 가장 많은 수와 그레이드
cnt, grade = 0, 0
# 책상에 앉은 학생들이 받아야 할 그레이드
desks = []
for _ in range(N):
    A, B = map(int, input().split())
    desks.append((A, B))

    # 다른 그레이드를 받을 때
    if A != B:
        # 연속성 체크 및 연속 개수 세기
        grades[A] += 1
        continues[A] = True
        grades[B] += 1
        continues[B] = True
    # 같은 그레이드를 받을 때
    else:
        grades[A] += 1
        continues[A] = True

    # 이전에 값이 부여된 것이 있다면 비교 후 초기화
    for i in range(1, 6):
        # 이전에 값이 부여되어 있다면 비교
        if grades[i]:
            if grades[i] > cnt:
                cnt = grades[i]
                grade = i
            elif grades[i] == cnt:
                if grade > i:
                    grade = i
            # 연속성이 없어졌다면 초기화
            if not continues[i]:
                grades[i] = 0
        # 연속성 초기화
        continues[i] = False

print(cnt, grade)












