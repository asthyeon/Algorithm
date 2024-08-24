import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 시간표 짜기 (14569))
 1. 비어 있는 시간에 추가로 신청할 수 있는 과목의 후보 개수 구하기
[입력]
 1. N: 총 과목 수
 2. N개의 줄: k: 각 과목의 수업시간의 수, k개의 숫자 t: 이 과목의 수업이 진행되는 교시
 3. M: 학생 수
 4. M개의 줄: p: 각 학생들의 비어 있는 교시 개수, p개의 숫자 q
[출력]
 1. M개의 줄에 걸쳐서 각 학생들의 들을 수 있는 과목 개수 출력
"""

"""
<풀이>
 1. 일단 풀어보기
 2. 제일 앞의 시간은 제외해야함
"""

N = int(input())
# 과목 리스트
subjects = []
for _ in range(N):
    k = list(map(int, input().split()))
    subjects.append(k[1:])

M = int(input())
for _ in range(M):
    p = list(map(int, input().split()))

    # 가능한 과목 수
    cnt = 0
    # 과목 순회
    for subject in subjects:
        for t in subject:
            # 학생의 시간표 안에 과목이 들어가지 않는다면 넘기기
            if t not in p[1:]:
                break
        # 이번 과목이 모두 성립된다면
        else:
            cnt += 1

    print(cnt)