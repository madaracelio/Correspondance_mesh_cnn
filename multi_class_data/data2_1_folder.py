import os
import glob
import shutil # python -m pip install pytest-shutil --no-cache-dir
from os.path import isfile, join, abspath

current_path = os.path.abspath(os.getcwd()) + "/"

def d21f(dir_path: str, dest_path: str, ext: str):
    if not os.path.exists(dest_path):
        os.mkdir(os.path.join(current_path, dest_path), 0o666)
        
    subfolders= [f.path.split("/")[1] + "/" for f in os.scandir(dir_path) if f.is_dir()]

    for sub in subfolders:
        #print(current_path + dir_path + sub)
        for jpgfile in glob.iglob(os.path.join(current_path + dir_path + sub, "*." + ext)):
            print(jpgfile)
            if not os.path.exists(os.path.join(jpgfile)):
                shutil.copy(jpgfile, os.path.abspath(os.path.join(current_path, dest_path)))

d21f("Train/", "Output/", "png")