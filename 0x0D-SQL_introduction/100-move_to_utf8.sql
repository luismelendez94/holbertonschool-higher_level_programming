-- Task 17: Go to UTF8
-- Converts database to UTF8 in your MySQL server
ALTER DATABASE htbn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY name TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
