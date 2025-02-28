CREATE TABLE Yield_Data(
     id SERIAL PRIMARY KEY,
     crop VARCHAR(100),
     state VARCHAR(100),
     year INT,
     yield_kg_per_ha DECIMAL(10,2)
);
