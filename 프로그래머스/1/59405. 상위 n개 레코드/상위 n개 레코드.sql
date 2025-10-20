-- 방법2) 서브쿼리 이용해보기 -> DATETIME에 대한 최소 값 이용
SELECT
    NAME
FROM
    ANIMAL_INS
WHERE
    DATETIME = (
        SELECT
            MIN(DATETIME)
        FROM
            ANIMAL_INS
    );

-- 방법1) 날짜에 대한 오름차순으로 정리한후 1개만 출력 -> LIMIT 이용
/* 
SELECT
    NAME
FROM 
    ANIMAL_INS
ORDER BY
    DATETIME ASC
LIMIT
    1; 
*/