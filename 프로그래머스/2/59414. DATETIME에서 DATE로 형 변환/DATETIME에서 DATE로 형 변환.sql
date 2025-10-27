-- DATE_FORMANT으로 날짜 형태 변경 -> DATE_FORMAT(날짜, '%Y-%M-%D'): Y, y, M, m, D, d
SELECT
    ANIMAL_ID,
    NAME,
    DATE_FORMAT(DATETIME, '%Y-%m-%d') AS 날짜
FROM
    ANIMAL_INS
ORDER BY
    ANIMAL_ID;