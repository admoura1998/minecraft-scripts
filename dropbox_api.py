import dropbox
import os
from secrets import TOKEN

dbx = dropbox.Dropbox(oauth2_access_token=TOKEN)
opt = os.getenv("OPERATION")

def upload_file(dbx, file, destination):
    with open(file, "rb+") as f:
        try:
            dbx.files_upload(f.read(), f"/{destination}.{file.split('.')[1]}", mode=dropbox.files.WriteMode.overwrite)
            exit(0)
        except dropbox.exceptions.ApiError as err:
            print(err)  


def download_file(dbx,host_path,path):
    try: 
        file = dbx.files_download_to_file(host_path+'/'+path.split('/')[1],path)
        exit(0)
    except dropbox.exceptions.ApiError as err:
        print(err)


if(opt == 0):
    upload_file(dbx, os.getenv("FILE"), os.getenv("DESTINATION"))
download_file(dbx, os.getenv("HOST_PATH"), os.getenv("PATH"))                        
    






    









