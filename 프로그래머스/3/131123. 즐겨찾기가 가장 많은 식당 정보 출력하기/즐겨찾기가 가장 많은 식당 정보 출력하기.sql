SELECT
    BASE.FOOD_TYPE,
    BASE.REST_ID,
    BASE.REST_NAME,
    BASE.FAVORITES
FROM
    REST_INFO BASE
    -- 기본 정보에 각 음식 종류별로 가장 즐겨찾기 수가 많은 테이블 조인
    LEFT JOIN (
        SELECT
            FOOD_TYPE,
            MAX(FAVORITES) AS MAX_FAVORITES
        FROM
            REST_INFO
        GROUP BY
            FOOD_TYPE
    ) MAXIMUM
    -- 음식 종류가 같은 경우에 한해서
    ON BASE.FOOD_TYPE = MAXIMUM.FOOD_TYPE
WHERE
    -- 즐겨찾기 수가 가장 많은 행들만 출력
    BASE.FAVORITES = MAXIMUM.MAX_FAVORITES
ORDER BY
    BASE.FOOD_TYPE DESC;