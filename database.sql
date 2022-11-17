DROP TABLE IF EXISTS symptoms CASCADE;
CREATE TABLE symptoms(
    disease_name TEXT,
    name TEXT
    );

DROP TABLE IF EXISTS disease CASCADE;
CREATE TABLE disease(
    code SERIAL,
    name TEXT,
    description TEXT,
    symptoms_name TEXT,
    death_rate double precision
);

DROP TABLE IF EXISTS medication CASCADE;
CREATE TABLE medication(
    disease_name TEXT,
    name TEXT PRIMARY KEY,
    cost DOUBLE PRECISION
);

DROP TABLE IF EXISTS patient CASCADE;
CREATE TABLE patient(
    user_id SERIAL,
    disease_name TEXT,
    symptoms_name TEXT,
    death TEXT,
    user_medication_name TEXT

);

DROP TABLE IF EXISTS commonTestAndProcedures CASCADE;
CREATE TABLE commonTestAndProcedures(
    name TEXT,
    disease_name TEXT

);



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