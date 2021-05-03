#!/bin/bash

readarray -t variables < variables.txt

#${variables[0]} img
#${variables[1]} container

docker stop ${variables[1]} && docker rm ${variables[1]} 

rm variables.txt
