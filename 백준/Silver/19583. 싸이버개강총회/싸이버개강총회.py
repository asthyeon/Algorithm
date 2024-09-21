import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 싸이버개강총회 (19583)
 1. 개강총회 시작 전, 학회원 입장 여부 확인(닉네임 체크)
  - 개강총회 시작 전 대화를 한 적이 있는 닉네임 보고 체크
  - 시작하자마자 채팅 기록을 남긴 학회원도 입장한 것
 2. 개강총회를 끝내고 나서, 스트리밍을 끝낼 때까지 퇴장 확인 여부 확인
  - 끝날 때까지 대화를 한 적이 있는 닉네임 보고 체크
  - 개강총회가 끝나자마자 채팅 기록을 남겨도 제 시간 퇴장
  - 개강총회 스트리밍이 끝나자마자 채팅 기록을 남겨도 제 시간 퇴장
 3. 00:00부터는 개강총회를 시작하기 전의 대기 시간
 4. 개강총회 스트리밍이 끝난 시간 이후로 남겨져 있는 기록은 X
[입력]
 1. S: 개총 시작 시간, E: 개총 끝낸 시간, Q: 개총 스트리밍 끝낸 시간
 2. 스트리밍 영상의 채팅 기록들이 시간순으로 주어짐
[출력]
 1. 출석이 확인된 학회원 인원 수 출력 
"""

"""
<풀이>
 1. 자료구조
"""

S, E, Q = map(str, input().split())
# 각 시간에 대한 시간과 분
S_hour = int(S[:2])
S_minute = int(S[3:])
E_hour = int(E[:2])
E_minute = int(E[3:])
Q_hour = int(Q[:2])
Q_minute = int(Q[3:])

# 입장 명단과 최종 출석 명단
entered = set()
attended = set()

while True:
    try:
        time, nick = map(str, input().split())
        # 시간과 분 나누기
        hour = int(time[:2])
        minute = int(time[3:])

        # 입장 체크
        if hour <= S_hour:
            # 시간이 같으면 분도 체크
            if hour == S_hour:
                if minute <= S_minute:
                    entered.add(nick)
            # 이전인 경우
            else:
                entered.add(nick)
            continue

        # 퇴장 체크
        if E_hour <= hour <= Q_hour:
            # 입장 체크가 된 회원이라면
            if nick in entered:
                # 시간이 다 같은 경우
                if E_hour == hour == Q_hour:
                    # 분이 사이에 있는 경우
                    if E_minute <= minute <= Q_minute:
                        attended.add(nick)
                # 개총 종료와 같은 경우
                elif hour == E_hour:
                    # 분이 같거나 이후
                    if minute >= E_minute:
                        attended.add(nick)
                # 스트리밍 종료와 같은 경우
                elif hour == Q_hour:
                    # 분이 같거나 이전
                    if minute <= Q_minute:
                        attended.add(nick)
                # 사이에 있는 경우
                else:
                    attended.add(nick)

    # 입력이 없을 때 종료
    except:
        break

print(len(attended))
