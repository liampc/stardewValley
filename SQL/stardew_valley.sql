CREATE DATABASE Stardew_valley;
USE Stardew_valley;

DROP DATABASE Stardew_valley;

CREATE TABLE Season (
	id INT NOT NULL AUTO_INCREMENT,
    season VARCHAR(20),
    PRIMARY KEY(id)
);

CREATE TABLE Crop (
	id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100),
    duration INT,
    season INT,
    PRIMARY KEY(id),
    FOREIGN KEY(season) REFERENCES Season(id)
);

CREATE TABLE Sells_for (
	crop_id INT NOT NULL,
    basic INT,
    silver INT,
    gold INT,
    iridium INT,
    per_day DECIMAL(6,2),
    PRIMARY KEY(crop_id),
    FOREIGN KEY(crop_id) REFERENCES Crop(id)
);

CREATE TABLE Energy (
	crop_id INT NOT NULL,
    basic INT,
    silver INT,
    gold INT,
    iridium INT,
    PRIMARY KEY(crop_id),
    FOREIGN KEY(crop_id) REFERENCES Crop(id)
);



CREATE TABLE Health (
	crop_id INT NOT NULL,
    basic INT,
    silver INT,
    gold INT,
    iridium INT,
    PRIMARY KEY(crop_id),
    FOREIGN KEY(crop_id) REFERENCES Crop(id)
);



CREATE TABLE Seller (
	id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100),
	PRIMARY KEY(id)
);


CREATE TABLE Buy_price (
	crop_id INT NOT NULL,
    price INT,
    seller INT,
    PRIMARY KEY(crop_id),
    FOREIGN KEY(crop_id) REFERENCES Crop(id),
    FOREIGN KEY(seller) REFERENCES Seller(id)
);

CREATE TABLE Seed (
	id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100),
    crop INT,
    PRIMARY KEY(id),
    FOREIGN KEY(crop) REFERENCES Crop(id)
);








