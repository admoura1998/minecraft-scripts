#!/bin/bash

docker run -d --name $1 \
            -v $2:/data \
	        -e EULA=true -e TYPE=$3 -e VERSION=$4 \
            -e MEMORY=$5 -e ONLINE_MODE=FALSE -e ENABLE_RCON=TRUE \
             -e RCON_PASSWORD=teste -e RCON_PORT=28016 \
            -p $6:$6 \
            $7
  




