import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 좌표 압축 (18870)
1. Xi를 좌표 압축 결과
 - X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 함

[풀이]
1. 정렬
2. 중복값은 세트로 제거후 딕셔너리로 랭크 부여
"""

N = int(input())
X = list(map(int, input().split()))

# 중복 제거
X_sort = sorted(list(set(X)))
# 랭크 부여
X_rank = {}
for i in range(len(X_sort)):
    X_rank[X_sort[i]] = i

# 정답 출력
for x in X:
    print(X_rank[x], end=' ')