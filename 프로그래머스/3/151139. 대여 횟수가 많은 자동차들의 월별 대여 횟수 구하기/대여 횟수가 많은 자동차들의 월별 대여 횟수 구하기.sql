SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(CAR_ID) AS RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY AS C
WHERE '2022-08-01' <= START_DATE AND START_DATE < '2022-11-01'
AND CAR_ID IN (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE '2022-08-01' <= START_DATE AND START_DATE < '2022-11-01'
    GROUP BY CAR_ID
    HAVING COUNT(CAR_ID) >= 5
)
GROUP BY MONTH(START_DATE), CAR_ID
HAVING COUNT(CAR_ID) > 0
ORDER BY MONTH(START_DATE) ASC, CAR_ID DESC;

