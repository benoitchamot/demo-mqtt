#!/bin/bash

# Create the sqlite3 file and add the messages table
cat create_table.sql | sqlite3 mqtt.db
