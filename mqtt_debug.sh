#!/bin/bash

# monitor receiving message
/usr/local/mosquitto/bin/mosquitto_sub -d -t "homeassistant/#"

# test sending message
/usr/local/mosquitto/bin/mosquitto_pub -h 192.168.1.100 -p 1883 -t "homeassistant/binary_sensor/garden/config" -m '{"name": "garden", "device_class": "motion"}'
