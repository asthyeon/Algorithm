import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 결혼식
 1. 상근이는 자신의 친구와 친구의 친구를 초대함
[입력]
 1. n: 동기의 수
 2. m: 리스트의 길이
 3. m개의 줄: 친구 관계 a, b
[출력]
 1. 결혼식에 초대하는 동기의 수 출력
"""

"""
<풀이>
 1. 딕셔너리 이용
"""


# 친구 초대
def invite(friend):
    # 초대된 친구가 아니라면 초대하고, 이미 초대된 친구라면 넘기기
    if friend not in invitation:
        invitation.add(friend)

    # 친구의 친구 조사
    for f in relationship[friend]:
        # 본인일 경우 넘기기
        if f == 1:
            continue
        # 아직 초대받지 못했다면 초대
        elif f not in invitation:
            invitation.add(f)
        # 이미 초대받았다면 넘기기
        else:
            continue




# 동기의 수 n
n = int(input())
# 리스트의 길이
m = int(input())
# 친구관계
relationship = {}
for _ in range(m):
    a, b = map(int, input().split())

    # a가 관계가 없으면 새로 형성, 있으면 추가
    if a not in relationship:
        relationship[a] = [b]
    else:
        relationship[a].append(b)

    # b가 관계가 없으면 새로 형성, 있으면 추가
    if b not in relationship:
        relationship[b] = [a]
    else:
        relationship[b].append(a)

# 초대장
invitation = set()
if 1 in relationship:
    for friend in relationship[1]:
        invite(friend)

print(len(invitation))