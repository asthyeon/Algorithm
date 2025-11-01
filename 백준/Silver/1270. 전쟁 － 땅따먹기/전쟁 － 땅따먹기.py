import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
<문제>
# 전쟁 - 땅따먹기 (1270)
1. 어느 땅에서 한 번호의 군대의 병사가 절반을 초과한다면 그 땅은 군대의 지배하에 놓임
2. 각 땅들을 지배한 군대의 번호 출력
 - 전쟁이 한창중인 땅이라면 "SYJKGW"을 쌍 따옴표 없이 출력
<풀이>
1. 구현 -> 딕셔너리 사용
 - 가장 큰 값이 여러 개 일때 처리 -> dict.values()로 큰 값 찾은 후 대조 (X)
 - 군대의 병사가 절반을 초과 -> 중복될 일이 없음
 - 가장 큰 값이 절반을 초과하는 지만 체크하기
2. 입력받을 때, 첫 번째 값과 나머지 값 따로 받기
 - '*'을 사용해서 첫 번째 값을 제외한 나머지 값은 리스트로
"""

# n: 땅의 개수
n = int(input())
for _ in range(n):
    # Ti: i번째 땅의 병사 수, soldiers: 각 병사들 수
    Ti, *soldiers = map(int, input().split())

    # 병사 수 세기
    counts = {}
    for i in range(Ti):
        if soldiers[i] not in counts:
            counts[soldiers[i]] = 0
        counts[soldiers[i]] += 1

    # 가장 큰 값에 대한 군인과 수 찾기 -> .items() 에서 기준을 lambda로 인덱스 1 값지정
    answer, maximum = max(counts.items(), key=lambda x: x[1])
    # 정답 조건
    if maximum > Ti / 2:
        print(answer)
    else:
        print('SYJKGW')