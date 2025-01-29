-- 코드를 입력하세요
SELECT
    AO.ANIMAL_ID,
    AO.NAME
FROM
    -- 입양 보낸 동물 테이블에 동물 보호소에 들어온 동물 테이블을 LEFT JOIN 하여 NULL 값 찾기
    ANIMAL_OUTS AO
    LEFT JOIN ANIMAL_INS AI
    ON AO.ANIMAL_ID = AI.ANIMAL_ID
WHERE
    AI.ANIMAL_ID IS NULL
ORDER BY
    AO.ANIMAL_ID;