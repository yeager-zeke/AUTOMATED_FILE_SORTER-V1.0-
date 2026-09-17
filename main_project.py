import os
import shutil
import time
print("THIS IS THE VERSION 1, WHICH IS ONLY OPTIMIZED FOR (IMAGES,PYTHON FILES,CFILES,TEXT FILES AND PDF FILES)")
time.sleep(2)
path=input("enter the full path :")
res=os.listdir(path)
for i in res:
    full_path=os.path.join(path,i)
    condition=os.path.isfile(full_path)
    if condition:
        name,extension=os.path.splitext(i)
        print([name,extension])
        if extension in [".png",".jpg"]:
            image_folder = os.path.join(path, "Images")
            os.makedirs(image_folder,exist_ok=True)
            destination=os.path.join(image_folder,i)
            shutil.move(full_path,destination)
        elif extension==".py":
            py_folder = os.path.join(path, "python files")
            os.makedirs(py_folder,exist_ok=True)
            destination=os.path.join(py_folder,i)
            shutil.move(full_path,destination)
        elif extension==".c":
            C_folder = os.path.join(path, "C files")
            os.makedirs(C_folder,exist_ok=True)
            destination=os.path.join(C_folder,i)
            shutil.move(full_path,destination)
        elif extension==".txt":
            txt_folder = os.path.join(path, "text files")
            os.makedirs(C_folder,exist_ok=True)
            destination=os.path.join(C_folder,i)
            shutil.move(full_path,destination)
        elif extension==".pdf":
            pdf_folder = os.path.join(path,"pdf files")
            os.makedirs(pdf_folder,exist_ok=True)
            destination=os.path.join(pdf_folder,i)
            shutil.move(full_path,destination)
        else:
            print("this filetype is not supported yet..")

            


    



