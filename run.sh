#!/bin/bash

docker run -d --name $1 \
            -v $2:/data \
	        -e EULA=true -e TYPE=$3 -e VERSION=$4 -e DIFFICULTY=$5 \
            -e MEMORY=$6 -e ONLINE_MODE=FALSE -e ENABLE_RCON=TRUE \
            -e RCON_PASSWORD=teste -e RCON_PORT=28016 -e SPAWN_PROTECTION=0 -e MODE=$7 \
            -p $8:25565 \
            $9
  




