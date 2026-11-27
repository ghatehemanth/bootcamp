# Vendor Payments Analysis – Key Insights

1. The dataset contains 41 records covering invoices from January to April 2026.
2. Invoice `INV1007` appears twice, indicating a duplicate invoice record.
3. A total of 16 invoices were paid after their due dates.
4. There are 10 pending invoices with no recorded payment date.
5. PostgreSQL continued using a Sequential Scan after the index was created because the table contains only 41 rows, making a full scan inexpensive.