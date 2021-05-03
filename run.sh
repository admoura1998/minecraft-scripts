#!/bin/bash

imageName="itzg/minecraft-server"
containerName="mserver"
serverFolder="/home/alvaro/Minecraft-Server"

docker run -d -it --name $containerName \
             -v $serverFolder:/data \
	     -e EULA=true -e TYPE=BUKKIT -e MEMORY=3G -e VERSION=1.16.5 \
	     -p 25565:25565 \
             $imageName

printf "$imageName\n$containerName">variables.txt


source ./plugins.sh
source ./properties.sh



