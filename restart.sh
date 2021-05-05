#!/bin/bash
readarray -t variables < variables.txt

docker restart ${variables[0]}
