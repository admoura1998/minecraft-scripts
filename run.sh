#!/bin/bash

docker run -d --name $1 \
             -v $2:/data \
	        -e EULA=true -e TYPE=BUKKIT -e VERSION=$3 -e MEMORY=$4 -e ONLINE_MODE=FALSE \            
	        -p $6:$6 \
            $5
  




