CREATE DATABASE IF NOT EXISTS house_price;
USE house_price;

CREATE TABLE IF NOT EXISTS prediction_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    OverallQual INT,
    GrLivArea FLOAT,
    GarageCars INT,
    TotalBsmtSF FLOAT,
    `1stFlrSF` FLOAT,
    YearBuilt INT,
    predicted_price FLOAT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM prediction_log;
