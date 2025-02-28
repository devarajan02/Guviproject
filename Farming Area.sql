CREATE TABLE Farming_Area(
     id SERIAL PRIMARY KEY,
     state VARCHAR(100),
     year INT,
     total_area_ha DECIMAL(12,2),
     cultivated_area_ha DECIMAL(12,2)
);