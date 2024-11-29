-- 코드를 작성해주세요
# 각 대장균별 형질 숫자를 2진수로 바꾸기
# 뒤에서부터 1번 순서
SELECT
    COUNT(ID) AS COUNT
FROM
    ECOLI_DATA
WHERE
    BIN(GENOTYPE) NOT LIKE '%1_'
    AND (
        BIN(GENOTYPE) LIKE '%1'
        OR BIN(GENOTYPE) LIKE '%1__'
    );