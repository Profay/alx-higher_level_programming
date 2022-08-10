-- script that creates a table called id_not_null in the current database in MySQL server
CREATE TABLE IF NOT EXISTS force_name (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
