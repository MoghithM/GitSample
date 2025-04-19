CREATE DATABASE prescription_db;
USE prescription_db;

CREATE TABLE prescriptions (
    patient_id INT,
    patient_name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    disease VARCHAR(100),
    medicine VARCHAR(100),
    prescription_date DATE
);
