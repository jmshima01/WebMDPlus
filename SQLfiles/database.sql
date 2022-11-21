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
    id SERIAL,
    name TEXT,
    age INTEGER,
    sex TEXT

);

DROP TABLE IF EXISTS tests_and_procedures CASCADE;
CREATE TABLE tests_and_procedures(
    disease_name TEXT,
    test_procedure TEXT
);

DROP TABLE IF EXISTS patient_symptoms CASCADE;
CREATE TABLE patient_symptoms(
    patient_id SERIAL,
    symptom TEXT
);

DROP TABLE IF EXISTS patient_medications CASCADE;
CREATE TABLE patient_medications(
    patient_id SERIAL,
    medication TEXT
);

DROP TABLE IF EXISTS patient_procedures CASCADE;
CREATE TABLE patient_procedures(
    patient_id SERIAL,
    procedure TEXT
);

-- ==================================
-- COPYING DATA INTO TABLES
\copy disease FROM 'disease_desc.csv' WITH(HEADER true, FORMAT csv);
\copy symptoms FROM 'symptoms.csv' WITH(HEADER true, FORMAT csv);
\copy disease_symptoms FROM 'symptoms_disease.csv' WITH(HEADER true, FORMAT csv);
\copy tests_and_procedures FROM 'commonTests_disease_mapping.csv' WITH(HEADER true, FORMAT csv);
\copy medication FROM 'medication_disease.csv' WITH(HEADER true, FORMAT csv);

-- CREATING PRIMARY AND FOREIGN KEYS
ALTER TABLE disease ADD PRIMARY KEY (name);
ALTER TABLE symptoms ADD PRIMARY KEY (name);

ALTER TABLE disease_symptoms ADD CONSTRAINT disease_fk FOREIGN KEY (disease_name) REFERENCES disease(name);
ALTER TABLE disease_symptoms ADD CONSTRAINT symptom_fk FOREIGN KEY (symptom) REFERENCES symptom(name);
ALTER TABLE disease_symptoms ADD PRIMARY KEY (disease_name, symptom);

ALTER TABLE tests_and_procedures ADD CONSTRAINT disease_procedure_fk FOREIGN KEY (disease_name) REFERENCES disease(name);
ALTER TABLE tests_and_procedures ADD PRIMARY KEY (disease_name, test_procedure);


ALTER TABLE medication ADD CONSTRAINT disease_medication_fk FOREIGN KEY (disease_name) REFERENCES disease(name);
ALTER TABLE medication ADD PRIMARY KEY (disease_name, medication_name);

ALTER TABLE patient ADD PRIMARY KEY (id);

ALTER TABLE patient_medications ADD CONSTRAINT patient_medication_fk FOREIGN KEY (patient_id) REFERENCES patient(id);
ALTER TABLE patient_medications ADD PRIMARY KEY (patient_id, medication);

ALTER TABLE patient_symptoms ADD CONSTRAINT patient_medication_fk FOREIGN KEY (patient_id) REFERENCES patient(id);
ALTER TABLE patient_symptoms ADD PRIMARY KEY (patient_id, symptom);

ALTER TABLE patient_procedures ADD CONSTRAINT patient_medication_fk FOREIGN KEY (patient_id) REFERENCES patient(id);
ALTER TABLE patient_procedures ADD PRIMARY KEY (patient_id, procedure);