#!usr/bin/env bash
# docker system prune -a
docker-compose -f docker-compose.prod.yaml up -d --build

echo "Success!!!"
