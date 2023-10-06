import sys
import shutil
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

def makedirs(root_path, dir_path):
        new_dir_path = root_path + dir_path
        p_newdir = Path (new_dir_path)
        p_newdir.mkdir(exist_ok=True)

def copy_file (root_path, source_path, img_path):
    dest_path = ROOT + img_path
    source_path = root_path + "/" + source_path
    p_file = Path (source_path)
    if p_file.is_file():
        shutil.move(source_path,dest_path)
    else:
        root_path = source_path
        findfiles (root_path)

def findfiles (root_path):
    p = Path (root_path)
    for i in p.iterdir():
        if i.suffix[1:].lower() in (images):
            img_path = "/Зображення"
            makedirs(ROOT, img_path)
            copy_file (root_path, i.name, img_path)

        elif i.suffix[1:].lower() in (video):
            img_path = "/Відео"
            makedirs(ROOT, img_path)
            copy_file (root_path, i.name, img_path)

        elif i.suffix[1:].lower() in (docs):
            img_path = "/Документи"
            makedirs(ROOT, img_path)
            copy_file (root_path, i.name, img_path)

        elif i.suffix[1:].lower() in (music):
            img_path = "/Музика"
            makedirs(ROOT, img_path)
            copy_file (root_path, i.name, img_path)

        elif i.suffix[1:].lower() in (archives):
            img_path = "/Архіви"
            makedirs(ROOT, img_path)
            copy_file (root_path, i.name, img_path)
 
        else:
            img_path = "/Інше"
            makedirs(ROOT, img_path)
            copy_file (root_path, i.name, img_path)

p = Path (path)
if p.is_dir():
    findfiles (path)

else:
    print ("the arg is not dir path")


