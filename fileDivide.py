import glob
import os
import random
import shutil


#dct = "C:\\Users\\pskavalekar\\Desktop\\DATASET\\captured-larged-dataset\\DCT\\all"
#lsbran = "C:\\Users\\pskavalekar\\Desktop\\DATASET\\captured-larged-dataset\\LSBRAN\\all"


#all_drectory = [dct,lsbran]

dir = "C:\\Users\\pskavalekar\\Desktop\\DATASET\\NEW-SET\\small-set\\DCT\\all"

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
"""
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