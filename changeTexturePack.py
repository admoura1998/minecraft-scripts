import re
import os

url="https://github.com/admoura1998/minecraft-texturepacks/blob/master/Clarity-1.16.zip?raw=true"
properties="/home/alvaro/Minecraft-Server/server.properties"
rsc="resource-pack="

def clearParameter(data):
    newData = re.sub(r"(?<={}).+".format(rsc), ' ', data, flags=re.M)
    with open(properties, 'w') as file:
        file.write(newData)
    return newData

def changeTxtPack():    
    with open(properties, 'r+') as file: 
        data = file.read()
        data = clearParameter(data)                                    
        newData = re.sub(r"^{}".format(rsc),rsc+url, data, flags=re.M)         
    with open(properties, 'w') as file:
        file.write(newData)                                                    

def main():
    changeTxtPack()

if __name__ == "__main__":
    main()
