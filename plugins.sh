#!/bin/bash

pluginsFolder="/home/alvaro/Minecraft-Server/plugins"
pluginsRepo="git@github.com:admoura1998/minecraft-plugins.git"
folder="minecraft-plugins"

if [ ! -d $folder ]
then
  git clone $pluginsRepo
  cd $folder; cp *.jar $pluginsFolder
else
  cd $folder ;  git reset --hard ; git checkout -- .; git stash save --keep-index --include-untracked;  git pull $pluginsRepo
  cp *.jar $pluginsFolder; cd ..
fi



