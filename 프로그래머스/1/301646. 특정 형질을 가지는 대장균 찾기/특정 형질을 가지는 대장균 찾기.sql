-- 개체 형질을 2진수로 변환 -> 자리수가 1인경우 형질 보유 
-- 2진수로 변환하기 위해 CONV(넣을 숫자, 넣을 숫자의 진법, 변환할 진법) or BIN(넣을 숫자) 사용
SELECT
    COUNT(ID) AS COUNT
FROM
    ECOLI_DATA
WHERE
    -- 2진법으로 전환했을 때 역순으로 형질 계산
    -- 2번 형질 미보유
    BIN(GENOTYPE) NOT LIKE '%1_'
    AND (
        -- 1번 형질 보유
        CONV(GENOTYPE, 10, 2) LIKE '%1'
        -- 3번 형질 보유
        OR CONV(GENOTYPE, 10, 2) LIKE '%1__'
    );