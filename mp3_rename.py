## rename audio file with metadata info

from tinytag import TinyTag
import os
from os import listdir
from os.path import isfile, join

music_ext = {".mp3", ".wma"}

onlyfiles = [f for f in listdir(".") if isfile(join(".", f))]
for i, name in enumerate(onlyfiles):
    filename, file_extension = os.path.splitext(name)
    if file_extension in music_ext:
        tag = TinyTag.get(name)
        t = tag.title
        a = tag.artist
        if t:
            os.rename(name, t)
            print('file %s renamed to %s.'%(filename, t+file_extension))
        elif a:
            os.rename(name, a+str(i))
            print('file %s renamed to %s.'%(filename, a+str(i)+file_extension))
