import os
import re
import fileinput
import sys

arch = os.getenv('SERVER_LIST_PATH')+"/server-list.properties"
server = os.getenv('SERVIDOR')

def removeServer(server):
    for line in fileinput.input(arch, inplace=1):
        sys.stdout.write(line.replace(server+",", ""))


def main():    
   removeServer(server)

if __name__ == "__main__":
    main()
