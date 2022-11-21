-- Go ahead and run interesting queries here!

--Queries w/o patient table
SELECT name, description, symptom
FROM disease d, disease_symptoms ds
WHERE d.name = ds.disease_name;

SELECT name, description, symptom
FROM disease d, disease_symptoms ds
WHERE d.name = ds.disease_name
  AND d.name ILIKE 'f%';

SELECT name, COUNT(symptom)
FROM disease d, disease_symptoms ds
WHERE d.name = ds.disease_name
GROUP BY d.name;
  
SELECT name, COUNT(symptom)
FROM disease d, disease_symptoms ds
WHERE d.name = ds.disease_name
  AND d.name IN 
  (SELECT disease_name FROM medication
   WHERE medication_name ILIKE '%ine'
        AND medication_name NOT ILIKE 'obsolete')
GROUP BY d.name;
