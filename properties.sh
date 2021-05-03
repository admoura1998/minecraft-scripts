#!/bin/bash
propertiesFolder="/home/alvaro/Minecraft-Server"
propertiesRepo="git@github.com:admoura1998/minecraft-properties.git"
folder="minecraft-properties"
if [ ! -d $folder ]
then
  git clone $propertiesRepo
  cd $folder ; cp server.properties $propertiesFolder  
else
  cd $folder ;  git reset --hard ; git checkout -- .; git stash save --keep-index --include-untracked;  git pull $propertiesRepo
  cp server.properties $propertiesFolder; cd ..  	
fi

