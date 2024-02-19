import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 거짓말(1043)
 1. 지민이는 거짓말을 하되, 진실을 아는 사람이 오면 진실로 이야기하기
 2. 지민이가 거짓말쟁이로 알려지지 않고, 거짓말을 할 수 있는 파티의 최댓값 구하기
[입력]
 1. N: 총 사람의 수, M: 파티의 수
 2. 진실을 아는 사람 수와 번호(1 ~ N)
 3. 3번째 줄 ~ M개의 줄: 각 파티마다 오는 사람 수와 번호(0 ~ N)
[출력]
 1. 문제의 정답 출력
"""

"""
<풀이>
 1. 파티에 오는 사람이 중복해서 올 수 있음
 2. 파티에 진실을 아는 사람이 있으면 다른 사람들도 진실을 알게 됨
 3. 딕셔너리 이용해보기 -> 나중에 진실을 알게 되는 사람이 생기면 이전 사람들도 리셋해야함
 4. 유니온 파인드 이용
"""


# find-set
def find(x):
    if people[x] == x:
        return x

    people[x] = find(people[x])
    return people[x]


# union-set
def union(x, y):
    x = find(x)
    y = find(y)

    # 둘다 진실을 아는 사람일 경우 넘기기
    if x in t_list and y in t_list:
        return

    # 진실을 아는 사람 중심으로 관계 형성
    elif x in t_list:
        people[y] = x
    elif y in t_list:
        people[x] = y

    # 진실을 모를 경우 작은 순서대로 관계 형성
    elif x > y:
        people[x] = y
    elif x < y:
        people[y] = x


# 총 사람 수 N, 파티 수 M
N, M = map(int, input().split())
# 진실을 아는 사람 수와 번호
truth = list(map(int, input().split()))
# 진실을 아는 사람 리스트
t_list = set(truth[1:])
# 사람 리스트
people = [i for i in range(N + 1)]

# 각 파티마다 오는 사람 수와 번호
parties = []
for _ in range(M):
    party = list(map(int, input().split()))
    parties.append(party[1:])
    # 관계 형성
    for j in range(1, party[0]):
        union(people[party[j]], people[party[j + 1]])

# 진실을 모르는 사람이 있는 파티 수 확인
answer = 0
for party in parties:
    for person in party:
        if find(person) in t_list:
            break
    else:
        answer += 1

print(answer)