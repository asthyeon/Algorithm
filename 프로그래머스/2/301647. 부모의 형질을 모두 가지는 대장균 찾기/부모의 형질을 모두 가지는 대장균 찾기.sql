-- 코드를 작성해주세요
SELECT
    A.ID,
    A.GENOTYPE,
    B.GENOTYPE AS PARENT_GENOTYPE
FROM
    ECOLI_DATA A
    -- 자식 정보가 있는 테이블에, 부모의 정보 테이블을 연결
    LEFT JOIN ECOLI_DATA B
    ON A.PARENT_ID = B.ID
WHERE
    -- 자식과 부모의 형질을 AND 연산 했을 때, 부모의 형질과 같을 때
    A.GENOTYPE & B.GENOTYPE = B.GENOTYPE
ORDER BY
    A.ID;