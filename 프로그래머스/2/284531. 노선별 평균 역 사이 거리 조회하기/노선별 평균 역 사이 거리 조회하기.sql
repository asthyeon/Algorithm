-- 총 누계거리: 역 사이 거리의 총합
-- GROUP BY의 경우 SELECT에서 '*'을 쓸 경우, 그룹화된 컬럼의 수가 더 적을 경우 오류 발생
-- CONCAT으로 'km' 붙이기
-- ROUND 함수 -> 정수를 넣을 시 해당 자리까지 나타내는 것
-- 정렬 기준 -> km가 포함된 문자열 X, 총 누계거리의 숫자값으로 

SELECT
    ROUTE,
    CONCAT(ROUND(SUM(D_BETWEEN_DIST), 1), 'km') AS TOTAL_DISTANCE,
    CONCAT(ROUND(AVG(D_BETWEEN_DIST), 2), 'km') AS AVERAGE_DISTANCE
FROM
    SUBWAY_DISTANCE
GROUP BY
    ROUTE
ORDER BY
    -- 정렬을 문자열이 아닌 숫자로 해야함
    SUM(D_BETWEEN_DIST) DESC;