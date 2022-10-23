#!usr/bin/env bash

docker-compose -f docker-compose.prod.yaml down
docker system prune -a -y
docker-compose -f docker-compose.prod.yaml up -d --build

echo "Success!!!"
