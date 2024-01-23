"""
# 풍선 터트리기
1. 풍선이 단 1개만 남을 때까지 계속 터트리기
 [1] 임의의 인접한 두 풍선 고르고 두 풍선 중 하나 터트리기
 [2] 터진 풍선으로 인해 풍선 사이에 빈 공간이 생기면 밀착 시키기
2. 인접한 두 풍선 중에서 번호가 더 작은 풍선을 터트리는 행위는 최대 1번만 가능
3. 위 규칙대로 풍선을 터트렸을 때 최후까지 남기는 것이 가능한 풍선들의 개수 찾기
* 입력
- a: 풍선 리스트
[출력: 최후까지 남기는 것이 가능한 풍선들의 개수]
"""

"""
@ 풀이
(1) 백트래킹 -> 시간초과
(2) 번호가 더 작은 풍선 터트리는 것 최대 1번 -> 시간초과
 - 좌우의 각 최소값보다 한 쪽이라도 작거나 같다면 생존가능
(3) 하나씩 탐색하며 break 걸기 -> 시간초과
(4) 각 시점에서의 최소값을 구해놓고 비교하기
"""


def solution(a):
    answer = 0
    
    # 최대값
    INF = 1000000001
    
    # 양쪽 끝은 무조건 만족
    answer += 2
    
    # 길이
    length = len(a)
    
    # 각 인덱스 지점의 좌측에서 최소값이 있는지 찾기
    # 좌측
    lefts = [INF] * length
    for l in range(1, length - 1):
        # 시작은 왼쪽 끝과 비교
        if l == 1:
            lefts[l - 1] = a[l - 1]
        lefts[l] = min(lefts[l - 1], a[l])

    # 우측
    rights = [INF] * length
    for r in range(length - 2, -1, -1):
        # 시작은 오른쪽 끝과 비교
        if r == length - 2:
            rights[r + 1] = a[r + 1]
        rights[r] = min(rights[r + 1], a[r])

    # 각 최소값보다 둘 다 크다면 생존 불가
    for i in range(1, length - 1):
        cnt = 0
        if a[i] > lefts[i]:
            cnt += 1
        if a[i] > rights[i]:
            cnt += 1
        
        if cnt < 2:
            answer += 1

    return answer