"""
[문제] 타겟 넘버
1. n개의 음이 아닌 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버 만들기
2. 맨 앞의 정수도 음수로 만들 수 있음

[풀이]
1. dfs 완전탐색 해보기
"""


def solution(numbers, target):
    answer = 0
    
    
    def dfs(numbers, target, now, turn):
        # 함수 안의 변수 사용
        nonlocal answer
        # 전체를 순회했다면 종료
        if turn == len(numbers):
            # target 값과 일치하면 +1
            if now == target:
                answer += 1
            return
        
        # 뺄셈
        dfs(numbers, target, now - numbers[turn], turn + 1)
        # 덧셈
        dfs(numbers, target, now + numbers[turn], turn + 1)
            
    
    # dfs 실행
    dfs(numbers, target, 0, 0)
    return answer