-- 코드를 입력하세요
#식품 아이디, 이름, 총매출 조회
# 조건 : 생산일자가 2022.05
SELECT p.product_id, p.product_name, (price*SUM(amount)) AS TOTAL_SALES
FROM food_product AS p JOIN food_order AS o ON p.product_id=o.product_id
WHERE MONTH(produce_date)='5' AND YEAR(produce_date)='2022'
GROUP BY p.product_id
ORDER BY TOTAL_SALES DESC, p.product_id