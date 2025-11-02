-- CASE로 여러 조건 나누기
-- 실제 날짜 형식이 예시와 다름 -> LIKE로 찾기
SELECT
    BOARD_ID,
    WRITER_ID,
    TITLE,
    PRICE,
    CASE
        WHEN STATUS = 'SALE' THEN '판매중'
        WHEN STATUS = 'RESERVED' THEN '예약중'
        ELSE '거래완료'
    END AS STATUS
FROM
    USED_GOODS_BOARD
WHERE
    CREATED_DATE LIKE '2022-10-05%'
ORDER BY
    BOARD_ID DESC;