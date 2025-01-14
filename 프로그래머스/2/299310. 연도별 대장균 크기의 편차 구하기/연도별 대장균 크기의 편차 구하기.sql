-- 코드를 작성해주세요
-- 분화된 연도별 대장균 크기의 편차 = 분화된 연도별 가장 큰 대장균의 크기 - 각 대장균의 크기
SELECT
    YEAR(A.DIFFERENTIATION_DATE) AS YEAR,
    B.BSIZE - A.SIZE_OF_COLONY AS YEAR_DEV,
    A.ID
FROM
    ECOLI_DATA A
    -- 분화된 연도별 가장 큰 대장균 크기를 구한 테이블을 JOIN
    LEFT JOIN (
        SELECT
            YEAR(DIFFERENTIATION_DATE) AS BYEAR,
            MAX(SIZE_OF_COLONY) AS BSIZE
        FROM
            ECOLI_DATA
        GROUP BY
            YEAR(DIFFERENTIATION_DATE)
    ) AS B ON YEAR(A.DIFFERENTIATION_DATE) = B.BYEAR
ORDER BY
    YEAR,
    YEAR_DEV;

    