"""
[문제] 체육복
1. 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있음
2. 최대한 많은 학생이 체육수업을 들어야 함
 - lost: 체육복 도난당한 학생들
 - reverse: 여벌 체육복을 가져온 학생들
3. 여벌 체육복을 가져온 학생이 도난당했을 수 있음

[풀이]
1. 여벌이 있는데, 도난 당한 사람을 예외 처리하기
"""

def solution(n, lost, reserve):
    answer = 0
    
    students = [1] * (n + 1)
    
    for l in lost:
        students[l] -= 1
    
    for r in reserve:
        students[r] += 1
    
    for i in range(1, n + 1):
        if i == 1:
            if students[i] == 0:
                if students[i + 1] > 1:
                    students[i] += 1
                    students[i + 1] -= 1
        elif i == n:
            if students[i] == 0:
                if students[i - 1] > 1:
                    students[i] += 1
                    students[i - 1] -= 1
        else:
            if students[i] == 0:
                if students[i - 1] > 1:
                    students[i] += 1
                    students[i - 1] -= 1
                elif students[i + 1] > 1:
                    students[i] += 1
                    students[i + 1] -= 1
                    
    for i in range(1, n + 1):
        if students[i] != 0:
            answer += 1
    return answer