-- A script that creates a new table @unique_id
-- The query creates a new table
CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1,
	name VARCHAR(256),
	UNIQUE(id)
)
