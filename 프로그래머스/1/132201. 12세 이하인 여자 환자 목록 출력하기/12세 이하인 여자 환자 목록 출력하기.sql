-- IFNULL 사용, 12세 이하, 여자환자도 출력해야함
SELECT
    PT_NAME,
    PT_NO,
    GEND_CD,
    AGE,
    IFNULL(TLNO, 'NONE') AS TLNO
FROM
    PATIENT
WHERE
    AGE <= 12 AND
    GEND_CD = 'W'
ORDER BY
    AGE DESC,
    PT_NAME ASC;