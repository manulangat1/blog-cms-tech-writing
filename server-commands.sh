#!usr/bin/env bash

docker-compose -f docker-compose.prod.yaml down  --rmi all
docker system prune -a -f -y
docker-compose -f docker-compose.prod.yaml pull
docker-compose -f docker-compose.prod.yaml up -d --build

echo "Success!!!"
