-- SQLite
CREATE TABLE IF NOT EXISTS ip (
id INTEGER PRIMARY KEY AUTOINCREMENT,
ip_number VARCHAR(255) NOT NULL,
ip_active INTEGER
)

SELECT id, ip_number, ip_active
FROM ip;

UPDATE ip SET ip_active = 0;

DELETE FROM ip;

SELECT ip_number FROM ip WHERE ip_active = 1 limit 1;

UPDATE ip SET ip_active = 0 WHERE ip_number = 'my_ip_number';