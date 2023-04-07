-- 코드를 입력하세요
SELECT MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE,'%Y-%m-%d') AS REVIEW_DATE
FROM MEMBER_PROFILE AS M JOIN REST_REVIEW AS R ON M.MEMBER_ID = R.MEMBER_ID
WHERE M.MEMBER_ID IN (SELECT MEMBER_ID
                        FROM REST_REVIEW
                        GROUP BY MEMBER_ID
                        HAVING COUNT(*) = (SELECT COUNT(*) AS TEMP
                                            FROM REST_REVIEW
                                            GROUP BY MEMBER_ID
                                            ORDER BY TEMP DESC LIMIT 1))
ORDER BY REVIEW_DATE, REVIEW_TEXT
