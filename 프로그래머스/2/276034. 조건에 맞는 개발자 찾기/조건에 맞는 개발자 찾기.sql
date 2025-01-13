-- 코드를 작성해주세요
# 비트연산 &(AND)를 이용하여 참인 경우만을 고르기
# 중복인 경우도 고려해야 함
SELECT
    DISTINCT(D.ID),
    D.EMAIL,
    D.FIRST_NAME,
    D.LAST_NAME
FROM
    DEVELOPERS D
    CROSS JOIN SKILLCODES S
WHERE
    D.SKILL_CODE & S.CODE
    AND S.NAME IN ('Python', 'C#')
ORDER BY
    D.ID;