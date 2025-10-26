-- DISTINCT로 중복 제거 -> NULL 값도 계산하지 않음
SELECT
    COUNT(DISTINCT NAME) AS 'count'
FROM
    ANIMAL_INS;