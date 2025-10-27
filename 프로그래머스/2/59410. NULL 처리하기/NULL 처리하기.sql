-- COALESCE 사용 -> COALESCE(넣을 값1, 넣을 값2, 넣을 값3, ...) 처음으로 NULL이 아닌 값 표시
SELECT
    ANIMAL_TYPE,
    COALESCE(NAME, 'No name') AS NAME,
    SEX_UPON_INTAKE
FROM
    ANIMAL_INS
ORDER BY
    ANIMAL_ID;