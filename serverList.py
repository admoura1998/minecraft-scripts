import os
import re

file = os.getenv('SERVER_LIST_PATH')+"/"+os.getenv('SERVER_LIST_FILE')
server = os.getenv('NOME_CONTAINER')

line="servers="

def clearParameter(data):
    newData = re.sub(r"(?<={}).+".format(line), ' ', data, flags=re.M)
    with open(file, 'w') as file:
        file.write(newData)
    return newData

def changeServerFile():    
    with open(file, 'r+') as file: 
        data = file.read()
        data = clearParameter(data)                                    
        newData = re.sub(r"^{}".format(line),rsc+server, data, flags=re.M)         
    with open(file, 'w') as file:
        file.write(newData)                                                    

def main():
    changeServerFile()

if __name__ == "__main__":
    main()










