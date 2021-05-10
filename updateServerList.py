import os
import re

# file = os.getenv('SERVER_LIST_PATH')+"/"+os.getenv('SERVER_LIST_FILE')
# server = os.getenv('NOME_CONTAINER')

arch="teste.txt"
line="servers="
server="mserver"

def changeServerFile():    
    with open(arch, 'r+') as file: 
        data = file.read()                                           
        newData = re.sub(r"^{}".format(line),line+server+',', data, flags=re.M)         
    with open(arch, 'w') as file:
        file.write(newData)                                                    

def main():
    changeServerFile()

if __name__ == "__main__":
    main()










