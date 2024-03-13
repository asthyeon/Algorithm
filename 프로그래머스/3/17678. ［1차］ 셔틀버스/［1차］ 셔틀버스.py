"""
# 셔틀버스
 1. 셔틀 규칙
  - 09:00 출발, 총 n회 t분 간격으로 역에 도착
  - 하나의 셔틀에는 최대 m명으 승객 탑승 가능
  - 셔틀은 도착했을 때 도착한 순간에 대기열에 선 크루까지 포함해서 대기 순서대로 태우고 바로 출발
 2. 콘은 같은 시간에 도착한 크루 중 대기열에서 제일 뒤에 있음
 3. 모든 크루는 23:59에 집에 돌아감(다음 날 셔틀을 타는 크루 X)
[입력]
 1. n: 셔틀 운행 횟수
 2. t: 셔틀 운행 간격
 3. m: 한 셔틀에 탑승 가능한 최대 크루 수
 4. timetable: 크루가 대기열에 도착하는 시간을 모은 배열(시간범위: 00:01 ~ 23:59)
[출력]
 1. 콘이 셔틀을 타서 사무실로 갈 수 있는 도착 시각 중 제일 늦은 시각
"""

"""
<풀이>
 1. 9시에 출발하는 점을 잘 고려하기
"""


def solution(n, t, m, timetable):
    answer = ''
    
    
    # 시간계산
    def clock(hour, minute, variable):
        if int(minute) + variable < 0:
            new_hour = int(hour) - 1
            new_minute = 60 + (int(minute) + variable)
        elif int(minute) + variable >= 60:
            new_hour = int(hour) + (int(minute) + variable) // 60
            new_minute = (int(minute) + variable) % 60
        else:
            new_hour = int(hour)
            new_minute = int(minute) + variable
        return f'{new_hour:02d}:{new_minute:02d}'
            
    
    # 시간순서대로 정리
    timetable.sort()
    
    # 버스가 1대일 때
    if n == 1:
        # 탑승인원이 탑승가능 수보다 더 적을 때
        if len(timetable) < m:
            answer = '09:00'
        # 탑승인원이 탑승가능 수보다 더 많거나 같을 때
        else:
            if timetable[m - 1] <= '09:00':
                answer = clock(timetable[m - 1][:2], timetable[m - 1][3:], -1)
            else:
                answer = '09:00'
                
    # 버스가 2대 이상일 때 마지막에 타는 사람만 고려하기
    else:
        # 누적 탑승 시간과 누적 탑승자 번호
        time = '09:00'
        number = 0
        # 현재 탑승자 수
        cnt = 0
        for bus in range(n):
            # 이번 버스가 만석이라면 종료
            for now in range(m):
                # 탑승자를 다 태웠다면 바로 종료
                if len(timetable) == number:
                    break
                if timetable[number] <= time:
                    number += 1
                    cnt += 1
            # 마지막 버스일 때
            if bus == n - 1:
                # 좌석이 남았다면 마지막 버스시간
                if cnt < m:
                    answer = time
                # 좌석이 남지 않았다면 마지막 탑승자 -1
                else:
                    answer = clock(timetable[number - 1][:2], timetable[number - 1][3:], -1)
            else: 
                cnt = 0
            # 버스 교체
            time = clock(time[:2], time[3:], t)
        
    return answer