-- TABLE CREATION
DROP TABLE IF EXISTS symptoms CASCADE;
CREATE TABLE symptoms(
    name TEXT
    );

DROP TABLE IF EXISTS disease CASCADE;
CREATE TABLE disease(
    name TEXT,
    description TEXT
);

CREATE TABLE disease_symptoms(
    disease_name TEXT,
    symptom TEXT
);

DROP TABLE IF EXISTS medication CASCADE;
CREATE TABLE medication(
    disease_name TEXT,
    medication_name TEXT
);

DROP TABLE IF EXISTS patient CASCADE;
CREATE TABLE patient(
    user_id SERIAL,
    disease_name TEXT,
    symptoms_name TEXT,
    death TEXT,
    user_medication_name TEXT

);

DROP TABLE IF EXISTS testsAndProcedures CASCADE;
CREATE TABLE testsAndProcedures(
    disease_name TEXT,
    test_procedure TEXT
);

-- ==================================
-- COPYING DATA INTO TABLES
\copy disease FROM 'disease_desc.csv' WITH(HEADER true, FORMAT csv);
\copy symptoms FROM 'symptoms.csv' WITH(HEADER true, FORMAT csv);
\copy disease_symptoms FROM 'symptoms_disease.csv' WITH(HEADER true, FORMAT csv);
\copy testsAndProcedures FROM 'commonTests_disease_mapping.csv' WITH(HEADER true, FORMAT csv);
\copy medication FROM 'medication_disease.csv' WITH(HEADER true, FORMAT csv);


-- DO NOT DELETE BELOW CODE!!!!!!

-- DROP TABLE IF EXISTS payment CASCADE;
-- CREATE TABLE payment(
--     payment_id SERIAL PRIMARY KEY,
--     user_id SERIAL,
--     name TEXT,
--     cost double precision,  -- might change to save space 
--     category_name TEXT,
--     subscription_type TEXT,
--     due_date DATE,
--     FOREIGN KEY (user_id) REFERENCES person(id),
--     FOREIGN KEY (category_name) REFERENCES category(name)

-- );

-- DROP TABLE IF EXISTS saving_goals CASCADE;
-- CREATE TABLE saving_goals(
--     user_id SERIAL DEFAULT NULL,
--     name TEXT,
--     amount double precision,
--     dead_line date,
--     FOREIGN KEY (user_id) REFERENCES person(id)
-- );

-- INSERT INTO saving_goals(name,amount,dead_line)
--     VALUES('bob','22.22','2022-02-22');