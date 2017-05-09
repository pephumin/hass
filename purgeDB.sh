#!/bin/bash

HOST='192.168.1.100'
DB='homeassistant'
USER='hass'
PASSWORD='12345'

# Delete older than 7 days
BEFORE=$(date --date="7 days ago" +%Y-%m-%d)" 00:00:00"

query="DELETE FROM states WHERE created < '$BEFORE'"
echo "$query" | mysql -h$HOST -D$DB -u$USER -p$PASSWORD

query="DELETE FROM events WHERE created < '$BEFORE'"
echo "$query" | mysql -h$HOST -D$DB -u$USER -p$PASSWORD
