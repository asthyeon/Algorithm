"""
[문제] H-Index
1. H-Index: 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값

[풀이]
1. 정렬
2. 기준점 h를 어떻게 잡는 지가 중요 -> 이진 탐색
3. 문제 오류 -> 이상, 이하 혼용되어 있음 but '입출력 예'에서는 이상, 미만으로 보는 것 같음
"""


def solution(citations):
    answer = 0
    
    
    def binary_search():
        # 가장 작은 값, 가장 큰 값, 정답
        start = 0
        end = max(citations)
        tmp = 0
        
        while start <= end:
            mid = (start + end) // 2
            
            # 이상, 미만 논문 카운트
            up = down = 0
            for citation in citations:
                # h 이상
                if citation >= mid:
                    up += 1
                # h 미만
                else:
                    down += 1
            
            # 조건을 만족하면 정답 갱신 및 간격 늘리기
            if up >= mid and down < mid:
                start = mid + 1
                tmp = mid
            # 조건을 만족하지 못하면 간격 줄이기
            else:
                end = mid - 1
        
        return tmp
                
        
    answer = binary_search()
    return answer