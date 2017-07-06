#!/bin/bash

docker run -d --name=watchtower -v /var/run/docker.sock:/var/run/docker.sock centurylink/watchtower --interval 82800 --cleanup

