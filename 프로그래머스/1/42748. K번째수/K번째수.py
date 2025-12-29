"""
[문제] K번째수
1. 배열을 i~j까지 자르고 정렬했을 때, k번째에 있는 수 구하기

[풀이]
1. 정렬
"""


def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        # 범위 설정 및 정렬
        new_array = array[commands[i][0] - 1:commands[i][1]]
        new_array.sort()
        
        # k번째 값 append
        answer.append(new_array[commands[i][2] - 1])
    
    return answer