#!/bin/bash

docker compose down -v
rm -rf pgdata
docker compose up -d --build
