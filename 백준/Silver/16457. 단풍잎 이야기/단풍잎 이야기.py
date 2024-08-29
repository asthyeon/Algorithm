import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 단풍잎 이야기 (16457)
 1. 각각의 퀘스트는 k개 스킬을 사용해야 완수 가능
 2. n개의 키에 스킬들을 배치할 수 있음
[입력]
 1. n: 키의 개수, m: 퀘스트의 개수, k: 퀘스트 당 사용해야 하는 스킬 수
 2. m개의 줄: 각각의 퀘스트에서 사용해야 하는 스킬들이 나옴
[출력]
 1. 가장 최적의 키배치를 했을 때 최대로 깰 수 있는 퀘스트의 개수 출력
"""

"""
<풀이>
 1. 조합
 2. n개의 키에 2n 개의 스킬들만 배치할 수 있음
"""
from itertools import combinations

n, m, k = map(int, input().split())
# 사용해야 할 스킬들
using = [i for i in range(1, 2 * n + 1)]
quests = []
for _ in range(m):
    needs = list(map(int, input().split()))
    quests.append(needs)

# 사용할 수 있는 키 조합
combinations = list(combinations(using, n))
# 최대로 깰 수 있는 퀘스트 개수
answer = 0
# 최적의 배치 찾기
for combination in combinations:
    cnt = 0
    # 퀘스트 순회
    for quest in quests:
        # 하나씩 순회
        for q in quest:
            # 조합에 해당이 안되면 종료
            if q not in combination:
                break
        # 전부 해당되면 cnt + 1
        else:
            cnt += 1

    # 최대값 갱신
    answer = max(answer, cnt)

print(answer)