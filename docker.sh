#!/bin/bash

docker run --name=hass --restart=always --net=host -itd  -v /volume1/docker/homeassistant:/config homeassistant/home-assistant:0.50
#docker run --name=hass --restart=always --net=host -itd  -v /volume1/docker/homeassistant:/config homeassistant/home-assistant:0.48.1 --link mysql:mysql

#docker run --name=mysql --rm -it --net=host mysql mysql -h 127.0.0.1 -uroot -p
