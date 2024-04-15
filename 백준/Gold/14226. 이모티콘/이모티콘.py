import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 이모티콘 (14226)
 0. 이미 화면에 이모티콘이 1개 존재하는 상태
 1. 3가지 연산으로 이모티콘 S개 만들기
 2. 3가지 연산
  - 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장
  - 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기
  - 화면에 있는 이모티콘 중 하나 삭제
 3. 모든 연산은 1초가 걸림
 4. 클립보드에 이모티콘을 복사하면 이전에 있던 내용은 덮어쓰기 됨
 5. 클립보드에 있는 이모티콘 중 일부를 삭제할 수 없음
 6. 화면에 이모티콘을 붙여넣기하면, 클립보드에 있는 이모티콘의 개수가 화면에 추가됨
[입력]
 1. S: 이모티콘을 보내야 하는 수
[출력]
 1. 이모티콘을 S개 만들기 위해 필요한 시간의 최솟값 출력
"""

"""
<풀이>
 1. 일단 풀어보기
"""
from collections import deque


def bfs():
    # 시간, 클립보드 상태, 이모티콘 수
    q = deque([(0, 0, 1)])
    # 중복 세트
    duple = set()
    duple.add((0, 0, 1))

    while q:
        time, clipboard, emoticon = q.popleft()

        # 연산 1 - 클립보드 덮어쓰기
        if (time + 1, emoticon, emoticon) not in duple:
            q.append((time + 1, emoticon, emoticon))
            duple.add((time + 1, emoticon, emoticon))

        # 연산 2 - 클립보드에 있는 이모티콘 화면에 붙여넣기
        if clipboard > 0:
            if (time + 1, clipboard, emoticon + clipboard) not in duple:
                q.append((time + 1, clipboard, emoticon + clipboard))
                duple.add((time + 1, clipboard, emoticon + clipboard))
                if emoticon + clipboard == S:
                    return time + 1

        # 연산 3 - 화면에 이모티콘 하나 삭제
        if emoticon - 1 > 0:
            if (time + 1, clipboard, emoticon - 1) not in duple:
                q.append((time + 1, clipboard, emoticon - 1))
                duple.add((time + 1, clipboard, emoticon - 1))
                if emoticon - 1 == S:
                    return time + 1


# 이모티콘을 보내야 하는 수 S
S = int(input())

print(bfs())
