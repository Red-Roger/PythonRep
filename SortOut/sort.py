import sys
import shutil
import re
import os
from pathlib import Path
for arg in sys.argv:
    path = arg

ROOT = path

images = ("jpg", "png", "jpeg", "svg")
video = ("avi", "mp4", "mov", "mkv")
docs = ("doc", "docx", "txt", "pdf", "xlsx", "pptx")
music = ("mp3", "ogg", "wav", "amr")
archives = ("zip", "rar", "tar", "gz")

def copy_file (root_path, source_path, img_path):
    dest_path = ROOT + img_path
    source_path = root_path + "/" + source_path
    p_file = Path (source_path)
    if p_file.is_file():
            shutil.move(source_path,dest_path)
    else:
        root_path = source_path
        findfiles (root_path)

def makedirs(root_path, dir_path):
        new_dir_path = root_path + dir_path
        p_newdir = Path (new_dir_path)
        p_newdir.mkdir(exist_ok=True)

def normalize(name):
    name = re.sub(r"[^+\w[.]", "_",name)
    return name

def findfiles (root_path):
    p = Path (root_path)
    for i in p.iterdir():
        name = normalize(i.name)
        old_name = root_path + "/" + i.name
        new_name = root_path + "/" + name
        os.rename(old_name, new_name)
        suffix = i.suffix
        if suffix[1:].lower() in (images):
            img_path = "/images"
            makedirs(ROOT, img_path)
            copy_file (root_path, name, img_path)

        elif i.suffix[1:].lower() in (video):
            img_path = "/video"
            makedirs(ROOT, img_path)
            copy_file (root_path, name, img_path)

        elif i.suffix[1:].lower() in (docs):
            img_path = "/documents"
            makedirs(ROOT, img_path)
            copy_file (root_path, name, img_path)

        elif i.suffix[1:].lower() in (music):
            img_path = "/audio"
            makedirs(ROOT, img_path)
            copy_file (root_path, name, img_path)

        elif i.suffix[1:].lower() in (archives):
            img_path = "/archives"
            makedirs(ROOT, img_path)
            copy_file (root_path, name, img_path)
 
        else:
            img_path = "/other"
            makedirs(ROOT, img_path)
            copy_file (root_path, name, img_path)

p = Path (path)
if p.is_dir():
    findfiles (path)

else:
    print ("the arg is not dir path")


