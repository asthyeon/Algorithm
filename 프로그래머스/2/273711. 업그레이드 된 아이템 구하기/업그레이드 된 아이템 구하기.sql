/*
희귀도가 'RARE'인 아이템들의 모든 다음 업그레이드 아이템 = PARENT가 있는 아이템
PARENT 아이템의 RARITY가 'RARE'이어야 함 -> PARENT_ITEM_ID로 조인 1번 더 하기
3번째 테이블의 PARENT_ITEM_ID의 RARITY가 RARE일 때,
1번째 테이블의 ITEM을 SELECT, PARENT가 없어도 두 번째 JOIN으로 인하여 제거됨
*/

SELECT
    A.ITEM_ID,
    A.ITEM_NAME,
    A.RARITY
FROM
    ITEM_INFO A
    LEFT JOIN ITEM_TREE B
        ON A.ITEM_ID = B.ITEM_ID
    JOIN ITEM_INFO C
        ON B.PARENT_ITEM_ID = C.ITEM_ID
WHERE
    C.RARITY = 'RARE'
ORDER BY
    A.ITEM_ID DESC;
