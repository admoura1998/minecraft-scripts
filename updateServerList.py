import os
import re
import fileinput
import sys

arch = os.getenv('SERVER_LIST_PATH')+"/"+os.getenv('SERVER_LIST_FILE')
server = os.getenv('NOME_CONTAINER')
line = "servers="

def updateServerFile(server):    
    with open(arch, 'r+') as file: 
        data = file.read()                                           
        newData = re.sub(r"^{}(.*)".format(line),line+server+',', data, flags=re.M)         
    with open(arch, 'w') as file:
        file.write(newData)  

def main():
    updateServerFile(server)
    

if __name__ == "__main__":
    main()










