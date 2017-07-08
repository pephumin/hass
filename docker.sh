#!/bin/bash

docker run --name=hass --restart=always --net=host -itd  -v /volume1/docker/homeassistant:/config homeassistant/home-assistant:0.48.1
