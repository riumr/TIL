SELECT * FROM playlist_track A ORDER BY PlaylistId DESC LIMIT 5;

SELECT * FROM tracks B ORDER BY TrackId LIMIT 5;

SELECT PlaylistId, Name FROM playlist_track join tracks
ON playlist_track.TrackId == tracks.TrackId
ORDER BY PlaylistId DESC LIMIT 5;

SELECT PlaylistId,Name FROM playlist_track join tracks
ON playlist_track.TrackId == tracks.TrackId
WHERE PlaylistId==10
ORDER BY Name DESC LIMIT 5;

SELECT COUNT(*) FROM tracks join artists
ON tracks.Composer == artists.Name;

SELECT COUNT(*) FROM tracks left join artists
ON tracks.Composer == artists.Name;

SELECT InvoiceLineId,InvoiceId FROM invoice_items
ORDER BY InvoiceId LIMIT 5;

SELECT InvoiceId,CustomerId FROM invoices
ORDER BY InvoiceId LIMIT 5;

SELECT invoice_items.InvoiceLineId,invoice_items.InvoiceId
FROM invoice_items join invoices
ON invoice_items.InvoiceId == invoices.InvoiceId
ORDER BY invoice_items.InvoiceId DESC LIMIT 5;

SELECT invoices.InvoiceId, invoices.CustomerId
FROM invoices join customers
ON invoices.CustomerId == customers.CustomerId
ORDER BY InvoiceId DESC LIMIT 5;

SELECT InvoiceLineId, invoice_items.InvoiceId, invoices.CustomerId
FROM invoice_items
		 JOIN invoices
		 ON invoice_items.InvoiceId == invoices.InvoiceId
		 JOIN customers
		 ON invoices.CustomerId = customers.CustomerId
ORDER BY invoice_items.InvoiceId DESC LIMIT 5;

SELECT customers.CustomerId, COUNT(*)
FROM customers 
		 JOIN invoices
     ON customers.CustomerId == invoices.CustomerId
     JOIN invoice_items
     ON invoices.invoiceId == invoice_items.invoiceId
GROUP BY customers.CustomerId
ORDER BY customers.CustomerId LIMIT 5;