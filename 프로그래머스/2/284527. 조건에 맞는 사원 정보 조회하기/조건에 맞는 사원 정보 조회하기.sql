-- 3개의 테이블 JOIN
-- 상, 하반기의 점수의 합을 구해야 함 -> 사번으로 GROUP BY
-- 내림차순으로 정렬 후, 상위 1개만 출력

SELECT
    SUM(SCORE) AS SCORE,
    HE.EMP_NO,
    HE.EMP_NAME,
    HE.POSITION,
    HE.EMAIL
FROM
    HR_DEPARTMENT HD
    JOIN HR_EMPLOYEES HE
        ON HD.DEPT_ID = HE.DEPT_ID
    JOIN HR_GRADE HG
        ON HE.EMP_NO = HG.EMP_NO
GROUP BY
    HE.EMP_NO
ORDER BY
    SCORE DESC
LIMIT
    1;