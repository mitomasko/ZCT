CREATE TABLE Datasets
(
    id INT NOT NULL PRIMARY KEY,
    temperature VARCHAR(50),
    luminosity VARCHAR(50),
    radius VARCHAR(50),
    absolute_magnitude VARCHAR(50),
    star_type VARCHAR(50),
    star_color VARCHAR(50),
    spectral_class VARCHAR(50)
);

USE database_zct

INSERT INTO Datasets (id, temperature, luminosity, radius, absolute_magnitude, star_type, star_color, spectral_class)
VALUES (1, '3068', '0.0024', '0.17', '16.12', '0', 'Red', 'M')

INSERT INTO Datasets (id, temperature, luminosity, radius, absolute_magnitude, star_type, star_color, spectral_class)
VALUES (2, '3042', '0.0005', '0.1542', '16.6', '0', 'Red', 'M')

INSERT INTO Datasets (id, temperature, luminosity, radius, absolute_magnitude, star_type, star_color, spectral_class)
VALUES (3, '2600', '0.0003', '0.102', '18.7', '0', 'Red', 'M')