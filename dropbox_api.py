import dropbox
import os
from secrets import TOKEN

dbx = dropbox.Dropbox(oauth2_access_token=TOKEN, app_key="n56k7vj4k8uwer3")
opt = os.getenv("OPERATION")
file = os.getenv("FILE")
destination = os.getenv("DESTINATION")
host_path = os.getenv("HOST_PATH")
path = os.getenv("PATH")

def upload_file(dbx, file, destination):
    with open(file, "rb+") as f:
        try:
            dbx.files_upload(f.read(), f"/{destination}.{file.split('.')[1]}", mode=dropbox.files.WriteMode.overwrite) 
            # dbx.files_upload(f.read(), f"/plugins-config.{file.split('.')[1]}", mode=dropbox.files.WriteMode.overwrite)          
        except dropbox.exceptions.ApiError as err:
            print(err)

def download_file(dbx,host_path,path):
    try: 
        file = dbx.files_download_to_file(host_path+'/'+path.split('/')[1],path)       
    except dropbox.exceptions.ApiError as err:
        print(err)       

print(f"OPERTATION -> {opt}")
print(f"FILE -> {file} ")
print(f"DESTINATION -> {destination} ")

if(opt == 0):
    upload_file(dbx, file, destination)
    exit(0)    
#download_file(dbx, host_path, path)                        
    






    









