
USE Stardew_valley;

## Testing disabling only full group by defaul
SET sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
#SET GLOBAL sql_mode=(SELECT CONCAT(@@sql_mode, ',ONLY_FULL_GROUP_BY'));
SELECT @@sql_mode;


SELECT * FROM Seller;

#How many crops are there for every season?
SELECT 
    Season.season AS 'Season',
    COUNT(Crop.id) AS 'Crops'
FROM Crop
JOIN Season ON Crop.season = Season.id
GROUP BY Season.season;
    

#What are the top 3 most expensive crop to sell?
SELECT 
	Crop.name AS 'Crop',
    SF.iridium AS 'Price',
    Season.season AS 'Season'
FROM Crop
JOIN Sells_for AS SF ON Crop.id = SF.crop_id
JOIN Season ON Crop.season = Season.id
ORDER BY SF.iridium DESC
LIMIT 3;




   







    
    





