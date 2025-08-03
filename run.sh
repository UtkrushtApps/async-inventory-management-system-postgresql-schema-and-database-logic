#!/bin/bash
set -e
cd /root/task
echo "Starting Docker containers..."
docker-compose up -d
# Wait for Postgres to be ready
PG_ISREADY="docker exec inventory_db pg_isready -U inventory_user -d inventory"
RETRIES=20
until $PG_ISREADY; do
  echo "Waiting for Postgres to be ready..."
  sleep 2
  RETRIES=$((RETRIES-1))
  if [ "$RETRIES" -eq 0 ]; then
    echo "Could not connect to Postgres, aborting."
    exit 1
  fi
done
# Schema and data
echo "Applying schema.sql..."
docker exec -i inventory_db psql -U inventory_user -d inventory < /root/task/schema.sql

echo "Applying sample_data.sql..."
docker exec -i inventory_db psql -U inventory_user -d inventory < /root/task/data/sample_data.sql

# Validate API is up
sleep 3
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/docs)
if [ "$HTTP_CODE" = "200" ]; then
  echo "FastAPI server is up and responding."
else
  echo "FastAPI server did not respond correctly."
  exit 2
fi
echo "Setup complete."
