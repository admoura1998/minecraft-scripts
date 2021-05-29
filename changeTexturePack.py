import re
import os

url =  '"' + os.getenv('URL') + '"'
properties = os.getenv('SERVER_DIRECTORY_HOST')+"/server.properties"

print(url)
print(properties)

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
