#!/usr/bin/env bash

docker rm -f gongfudou

docker rmi -f gongfudou

docker build -t gongfudou .

docker run -d --name gongfudou gongfudou