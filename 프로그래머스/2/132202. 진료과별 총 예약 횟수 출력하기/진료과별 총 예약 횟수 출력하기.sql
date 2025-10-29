-- GROUP BY 사용, 예약 날짜 유의
-- HAVING은 그룹화되지 않은 컬럼에 대해서는 사용 불가 -> WHERE에서 사용
-- WHERE 절 다음에 GROUP BY 절이 와야 함
SELECT
    MCDP_CD AS 진료과코드,
    COUNT(*) AS 5월예약건수
FROM
    APPOINTMENT
WHERE
    APNT_YMD LIKE '2022-05%'
GROUP BY
    MCDP_CD
ORDER BY
    5월예약건수 ASC,
    진료과코드 ASC;