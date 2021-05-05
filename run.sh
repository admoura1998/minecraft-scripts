#!/bin/bash

docker run --name $1 \
             -v $2:/data \
	        -e EULA=true -e TYPE=BUKKIT -e VERSION=$3 -e MEMORY=$4 \
	        -p 25565:25565 \
            $5

printf "$1">variables.txt



