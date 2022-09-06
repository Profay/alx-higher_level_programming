-- This script creates the table unique_iD
CREATE TABLE IF NOT EXISTS unique_id (
    id   INT          DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
