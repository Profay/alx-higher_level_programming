-- script that creates a table called id_not_null in the current database in MySQL server
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
