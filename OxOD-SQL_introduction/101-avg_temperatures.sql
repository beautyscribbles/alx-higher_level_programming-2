-- displays the avg temperature (Fahrenheit) by city ordered by temperature (descending)
-- then displays an average value
SELECT `city`, AVG(`value`) 'avg_temp' FROM temperatures GROUP BY `city` ORDER BY `avg_temp` DESC;
