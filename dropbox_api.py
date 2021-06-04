import dropbox
import os
from secrets import TOKEN

dbx = dropbox.Dropbox(oauth2_access_token=TOKEN, app_key="n56k7vj4k8uwer3")

print(f"DBX -> {dbx}")

opt = int(os.getenv("OPERATION"))
file = os.getenv("FILE")
destination = os.getenv("DESTINATION")
host_path = os.getenv("HOST_PATH")
path = os.getenv("PATH")

def upload_file(dbx, file, destination):
    with open(file, "rb+") as f: 
        try:       
            dbx.files_upload(f.read(), f"/{destination}.{file.split('.')[1]}", mode=dropbox.files.WriteMode.overwrite)
            exit(0)
        except dropbox.exceptions.ApiError as err:
            print(err)
            exit(1)

def download_file(dbx,host_path,path): 
    try:   
        file = dbx.files_download_to_file(host_path+'/'+path.split('/')[1],path)       
    except dropbox.exceptions.ApiError as err:
            print(err)
            exit(1) 

if opt == 0:
    upload_file(dbx, file, destination)
download_file(dbx, host_path, path)   
                      
    






    









