#dct = "C:\\Users\\pskavalekar\\Desktop\\DATASET\\captured-larged-dataset\\DCT\\all"
#lsbran = "C:\\Users\\pskavalekar\\Desktop\\DATASET\\captured-larged-dataset\\LSBRAN\\all"


#all_drectory = [dct,lsbran]
import glob
import os
import random
import shutil


lsb = "C:\\Users\\pskavalekar\\Desktop\\DATASET\\NEW-set-internet\\small-set\\test 2\\lcb\\all"
dct ="C:\\Users\\pskavalekar\\Desktop\\DATASET\\NEW-set-internet\\small-set\\test 2\\dct\\all"
lsbran ="C:\\Users\\pskavalekar\\Desktop\\DATASET\\NEW-set-internet\\small-set\\test 2\\lcbran\\all"

dirs = [lsb,lsbran,dct]


paths = dirs[2]

print(paths)
"""
if os.path.exists(paths):

    os.chdir(paths)

    if os.path.isdir(paths) is True:
            
        #train
        os.makedirs(os.path.join(paths,"train\\NORMAL"))
        os.makedirs(os.path.join(paths,"train\\STEGGED"))
            
        #test
        os.makedirs(os.path.join(paths,"test\\NORMAL"))
        os.makedirs(os.path.join(paths,"test\\STEGGED"))
            
        #valid
        os.makedirs(os.path.join(paths,"valid\\NORMAL"))
        os.makedirs(os.path.join(paths,"valid\\STEGGED"))

        #train
        for c in random.sample(glob.glob('cap *'), 468):
            shutil.move(c,"train\\NORMAL")
        for c in random.sample(glob.glob('stegged *'), 1404):
            shutil.move(c,"train\\STEGGED")

        #test
        for c in random.sample(glob.glob('cap *'), 59):
            shutil.move(c,"test\\NORMAL")
        for c in random.sample(glob.glob('stegged *'), 175):
            shutil.move(c,"test\\STEGGED")

        #valid
        for c in random.sample(glob.glob('cap *'), 58):
            shutil.move(c,"valid\\NORMAL")
        for c in random.sample(glob.glob('stegged *'), 174):
            shutil.move(c,"valid\\STEGGED")
    
print("done")

"""

os.chdir(paths)
if os.path.isdir(paths) is True:
    os.makedirs(os.path.join(paths,"train\\NORMAL"))
    os.makedirs(os.path.join(paths,"train\\STEGGED"))
    os.makedirs(os.path.join(paths,"test\\NORMAL"))
    os.makedirs(os.path.join(paths,"test\\STEGGED"))
    os.makedirs(os.path.join(paths,"valid\\NORMAL"))
    os.makedirs(os.path.join(paths,"valid\\STEGGED"))
    
    for c in random.sample(glob.glob('normal *'), 480):
        shutil.move(c,"train\\NORMAL")
    for c in random.sample(glob.glob('stegged *'), 480):
        shutil.move(c,"train\\STEGGED")
    
    for c in random.sample(glob.glob('normal *'), 60):
        shutil.move(c,"test\\NORMAL")
    for c in random.sample(glob.glob('stegged *'), 60):
        shutil.move(c,"test\\STEGGED")
    
    for c in random.sample(glob.glob('normal *'), 60):
        shutil.move(c,"valid\\NORMAL")
    for c in random.sample(glob.glob('stegged *'), 60):
        shutil.move(c,"valid\\STEGGED")


print("done")



"""

if os.path.exists(dir):

    os.chdir(dir)

    if os.path.isdir(dir) is True:

        #train
        os.makedirs(os.path.join(dir,"train\\NORMAL"))
        os.makedirs(os.path.join(dir,"train\\STEGGED"))
            
        #test
        os.makedirs(os.path.join(dir,"test\\NORMAL"))
        os.makedirs(os.path.join(dir,"test\\STEGGED"))
            
        #valid
        os.makedirs(os.path.join(dir,"valid\\NORMAL"))
        os.makedirs(os.path.join(dir,"valid\\STEGGED"))

        for c in random.sample(glob.glob('cap *'), 8):
            shutil.move(c,"dct")
        for c in random.sample(glob.glob('cap *'), 9):
            shutil.move(c,"lsb")
        for c in random.sample(glob.glob('cap *'), 8):
            shutil.move(c,"randomlasb")

if os.path.exists(dir):

    os.chdir(dir)

    if os.path.isdir(dir) is True:
        os.makedirs(os.path.join(dir,"NORMAL"))
        os.makedirs(os.path.join(dir,"STEGGED"))


        for c in random.sample(glob.glob('cap *'), 312):
            shutil.move(c,"NORMAL")
        for c in random.sample(glob.glob('stegged *'), 312):
            shutil.move(c,"STEGGED")


print("done")




if os.path.exists(dir):

    os.chdir(dir)
    if os.path.isdir(dir) is True:
        os.makedirs(os.path.join(dir,"toSteggForsmall"))

        for c in random.sample(glob.glob('car *'), 120):
            shutil.move(c,"toSteggForsmall")

print("done")



os.chdir(dir)
if os.path.isdir(dir) is True:
    os.makedirs(os.path.join(dir,"train\\NORMAL"))
    os.makedirs(os.path.join(dir,"train\\STEGGED"))
    os.makedirs(os.path.join(dir,"test\\NORMAL"))
    os.makedirs(os.path.join(dir,"test\\STEGGED"))
    os.makedirs(os.path.join(dir,"valid\\NORMAL"))
    os.makedirs(os.path.join(dir,"valid\\STEGGED"))
    
    for c in random.sample(glob.glob('cap *'), 499):
        shutil.move(c,"train\\NORMAL")
    for c in random.sample(glob.glob('stegged *'), 468):
        shutil.move(c,"train\\STEGGED")
    
    for c in random.sample(glob.glob('cap *'), 61):
        shutil.move(c,"test\\NORMAL")
    for c in random.sample(glob.glob('stegged *'), 58):
        shutil.move(c,"test\\STEGGED")
    
    for c in random.sample(glob.glob('cap *'), 62):
        shutil.move(c,"valid\\NORMAL")
    for c in random.sample(glob.glob('stegged *'), 59):
        shutil.move(c,"valid\\STEGGED")


print("done")


os.chdir(dir)
if os.path.isdir(dir) is True:
    os.makedirs(os.path.join(dir,"stegging"))

    for c in random.sample(glob.glob('car *'), 60):
        shutil.move(c,"stegging")



print("done")


#!/usr/bin/python
from PIL import Image
import os, sys
from progress.bar import Bar

path = "C:\\Users\\pskavalekar\\Desktop\\DATASET\\InternetDataset\\baseballcapresize"
outputPath = "C:\\Users\\pskavalekar\\Desktop\\DATASET\\InternetDataset\\resize1"

dirs = os.listdir( path )


def resize():
    bar = Bar('Processing', max=len(dirs))
    for item in dirs:
        final_path= os.path.join(path,item)
        
        if os.path.exists(final_path):
            im = Image.open(final_path)
            print(" resizing "+final_path)
            f, e = item.split(".")
            imResize = im.resize((2176,4608), Image.Resampling.LANCZOS)
            imResize.save(outputPath+"\\"+f + ' resized.png', 'PNG', quality=90)
            bar.next()

    bar.finish()

resize()


#!/usr/bin/python
from PIL import Image
import os, sys
from progress.bar import Bar

path = "C:\\Users\\pskavalekar\\Desktop\\DATASET\\NEW-set-internet"
outputPath = "C:\\Users\\pskavalekar\\Desktop\\DATASET\\resize-car"

dirs = os.listdir( path )


def resize():
    bar = Bar('Processing', max=len(dirs))
    for item in dirs:
        final_path= os.path.join(path,item)
        
        if os.path.exists(final_path):
            im = Image.open(final_path)
            print(" resizing "+final_path)
            f, e = item.split(".")
            imResize = im.resize((2176,4608), Image.Resampling.LANCZOS)
            imResize.save(outputPath+"\\"+f + ' resized.png', 'PNG', quality=90)
            bar.next()

    bar.finish()

resize()"""

