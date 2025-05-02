-- Create the messages table to store the MQTT messages
-- Execute this in a sqlite3 file called mqtt.db
CREATE TABLE messages (
    timestamp DATETIME,
    topic TEXT,
    tag TEXT,
    value TEXT,
    units TEXT,
    created_at DATETIME
);
