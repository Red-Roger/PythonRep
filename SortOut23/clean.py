
import shutil
import re
import os
from pathlib import Path 
import sys
from threading import Thread


CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
            "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

images = ("jpg", "png", "jpeg", "svg")
video = ("avi", "mp4", "mov", "mkv")
docs = ("doc", "docx", "txt", "pdf", "xlsx", "pptx")
music = ("mp3", "ogg", "wav", "amr")
archives = ("zip", "rar", "tar", "gz")


def copy_file (root_path, source_path, img_path, ROOT):
    dest_path = ROOT + img_path
    d_file = Path (dest_path + "/" + source_path)
    source_path = root_path + "/" + source_path
    p_file = Path (source_path)
    if p_file.is_file():
        if d_file.exists() == False:
            if p_file.suffix[1:] in (archives):
                shutil.unpack_archive (p_file.name, dest_path + "/" + p_file.stem)
                os.remove(source_path)
            else:
                shutil.move(source_path,dest_path)
    else:
        root_path = source_path
        findfiles (root_path, ROOT)

def del_dirs(path):
    for d in os.listdir (path):
        a = os.path.join (path, d)
        if os.path.isdir (a):
            del_dirs(a)
            if not os.listdir(a):
                os.rmdir(a)

def makedirs(root_path, dir_path):
        new_dir_path = root_path + dir_path
        p_newdir = Path (new_dir_path)
        p_newdir.mkdir(exist_ok=True)

def normalize(name):
    name = re.sub(r"[^+\w[.]", "_",name)
    TRANS = {}
    for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = l
        TRANS[ord(c.upper())] = l.title()
    name = name.translate(TRANS)
    return name


def findfiles (root_path, ROOT):

    p = Path (root_path)

    for i in p.iterdir():
        name = normalize(i.name)
        old_name = root_path + "/" + i.name
        new_name = root_path + "/" + name
        os.rename(old_name, new_name)
        suffix = i.suffix

        if suffix[1:].lower() in (images):
            img_path = "/images"

        elif i.suffix[1:].lower() in (video):
            img_path = "/video"

        elif i.suffix[1:].lower() in (docs):
            img_path = "/documents"

        elif i.suffix[1:].lower() in (music):
            img_path = "/audio"

        elif i.suffix[1:].lower() in (archives):
            img_path = "/archives"
                
        else:
            img_path = "/other"
        
        makedirs(ROOT, img_path)
        
        threads = []
        thread = Thread(target=copy_file (root_path, name, img_path, ROOT))
        thread.start()
        threads.append(thread) #про всяк випадок зберегти потоки )


def main():
    for arg in sys.argv:
        path = arg
    p = Path (path)
    ROOT = path
    if p.is_dir():
        thread2 = Thread(target=findfiles (path, ROOT))
        thread2.start()
        del_dirs(path) 
    else:
        print ("the arg is not dir path")
  
       
if __name__ == '__main__':
    main()


