#!usr/bin/env bash
docker system prune -a
docker-compose -f docker-compose.prod.yml up -d --build

echo "Success!!!"
