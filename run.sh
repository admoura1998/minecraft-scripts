#!/bin/bash

docker run -d --name $1 \
            -v $2:/data \
	        -e EULA=true -e TYPE=BUKKIT -e VERSION=$3 \
            -e MEMORY=$4 -e ONLINE_MODE=FALSE -e ENABLE_RCON=true -e RCON_PASSWORD=teste \
            -e RCON_PORT=28016
            -p $5:$5 \
            $6
  




