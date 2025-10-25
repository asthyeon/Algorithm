-- IF 절 사용
SELECT
    HISTORY_ID,
    CAR_ID,
    DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE,
    DATE_FORMAT(END_DATE, '%Y-%m-%d') AS END_DATE,
    -- 대여한 당일부터 1일이므로 29일 이상부터 카운트
    -- '-'로는 날짜를 정수화하여 뺀 값만 계산하므로, 정확한 일수 계산을 위해 DATEDIFF 사용해야 함
    -- END_DATE에서 START_DATE를 DIFF해야 양수값이 나옴
    IF(DATEDIFF(END_DATE, START_DATE) >= 29, '장기 대여', '단기 대여') AS RENT_TYPE
FROM
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE
    START_DATE LIKE '2022-09%'
ORDER BY
    HISTORY_ID DESC;