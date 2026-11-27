-- 1. Find the top 5 vendors by total invoice amount
SELECT
    vendor_name,
    SUM(amount) AS total_amount
FROM vendor_payments
GROUP BY vendor_name
ORDER BY total_amount DESC
LIMIT 5;

SELECT 
	invoice_id,
	COUNT(*) AS occurrences
FROM vendor_payments
GROUP BY invoice_id
HAVING COUNT(*)>1;

SELECT DATE_TRUNC('month', invoice_date) AS month,
    SUM(amount) AS monthly_total
FROM vendor_payments
GROUP BY month
ORDER BY month;

SELECT due_date,
    payment_date,
    invoice_id,
    vendor_name
FROM vendor_payments
WHERE payment_date > due_date;

SELECT department,
    SUM(amount) AS total_amount
FROM vendor_payments
GROUP BY department
ORDER BY total_amount DESC;

SELECT status,
    COUNT(*) AS total_pending
FROM vendor_payments
GROUP BY status;

SELECT vendor_name,
    COUNT(*) AS total_invoices
FROM vendor_payments
GROUP BY vendor_name
ORDER BY total_invoices DESC;

SELECT vendor_name,
    AVG(amount) AS average_amount
FROM vendor_payments
GROUP BY vendor_name
ORDER BY average_amount DESC;

SELECT SUM(amount) AS pending_amount
FROM vendor_payments
WHERE status='Pending';

SELECT invoice_id,
    vendor_name,
    due_date,
    amount
FROM vendor_payments
WHERE status='Pending'
AND CURRENT_DATE>due_date;