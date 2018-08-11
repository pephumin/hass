#!/bin/bash

docker run -d --name=hass -v /volume1/docker/home-assistant:/config -e "TZ=Thailand/Bangkok" -p 8123:8123 homeassistant/home-assistant:0.75.3

docker run --name tasmoadmin --restart=always --net=host -tid -v /volume1/docker/mqtt/config:/mqtt/config:ro -v /volume1/docker/mqtt/log:/mqtt/log -v /volume1/docker/mqtt/data/:/mqtt/data/ toke/mosquitto
