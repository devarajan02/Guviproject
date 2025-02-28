CREATE TABLE Yield_Data(
     id SERIAL PRIMARY KEY,
     crop VARCHAR(100),
     state VARCHAR(100),
     year INT,
     yield_kg_per_ha DECIMAL(10,2)
);
CREATE TABLE Farming_Area(
     id SERIAL PRIMARY KEY,
     state VARCHAR(100),
     year INT,
     total_area_ha DECIMAL(12,2),
     cultivated_area_ha DECIMAL(12,2)
);
CREATE TABLE Farming_Area(
     id SERIAL PRIMARY KEY,
     state VARCHAR(100),
     year INT,
     total_area_ha DECIMAL(12,2),
     cultivated_area_ha DECIMAL(12,2)
);
