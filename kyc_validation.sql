-- View all records
SELECT * FROM kyc_data;

-- Find duplicate KYC records
SELECT PAN, Aadhaar, COUNT(*) AS duplicate_count
FROM kyc_data
GROUP BY PAN, Aadhaar
HAVING COUNT(*) > 1;

-- Identify missing PAN or Aadhaar
SELECT *
FROM kyc_data
WHERE PAN IS NULL OR Aadhaar IS NULL;

-- Find underage or invalid age customers
SELECT *
FROM kyc_data
WHERE Age < 18 OR Age > 100;

-- Detect invalid email formats
SELECT *
FROM kyc_data
WHERE Email NOT LIKE '%@%';

-- KYC status summary
SELECT KYC_Status, COUNT(*) AS total
FROM kyc_data
GROUP BY KYC_Status;
