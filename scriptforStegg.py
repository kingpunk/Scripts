"""
Things to do in this script
1.Generate Random text (Huge)
1. Get the Total number of files in a directory
2. Generate random text
3. Convert text to binary
4. Start encoding with LHS for each text
5. Done
decoder not priority now
"""
from fileinput import filename
from msilib.schema import File
import os
from os.path import isfile,join
import cv2
import numpy as np
import random
import stegano
<<<<<<< HEAD
import string
=======
>>>>>>> 7f57d6394d4f3c131e6b2c92a80cd28992c218f0

verbose = False

def generateRandomString(randomTextSize):
<<<<<<< HEAD
    lowerCaseLetters = string.ascii_lowercase
    uppderCaseLetters = string.ascii_uppercase
    letters= string.ascii_letters
    digits = string.digits
    punctuations = string.punctuation
    all = [lowerCaseLetters,uppderCaseLetters,letters,digits,punctuations]

    
    text = ''

    for i in range(randomTextSize):
        text += ''.join([random.choice(i) for i in all])
=======
    nouns = ("puppy", "car", "rabbit", "girl", "monkey")
    verbs = ("runs", "hits", "jumps", "drives", "barfs")
    adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.")
    adj = ("adorable", "clueless", "dirty", "odd", "stupid")
    all = [nouns, verbs, adj, adv]

    text = ''

    for i in range(randomTextSize):
        text += ' '.join([random.choice(i) for i in all])
>>>>>>> 7f57d6394d4f3c131e6b2c92a80cd28992c218f0
    
    return text




def encode(ImageName,randomTextSize,outputLocation,Filename):
    #get Filename, extension, path
    count = 0
    try:
        outputDirectory = "OutputStegg"
        path=os.path.join(outputLocation,outputDirectory)
        os.mkdir(path)
    except:
        raise Exception("Something is wrong with Output file location")
    for files in ImageName:

        #read the image
    

        image = cv2.imread(files)   
        #get maximum bytes to encode
        n_byte = image.shape[0] * image.shape[1] * 3 // 8
        file, ext = Filename[count].split(".")
<<<<<<< HEAD
        print("stegging "+ file+"."+ext+" in progess....")
        #print("Maximum bytes to encode for "+ file+"."+ext+" is "+n_byte)
        print("\n")
=======
        if verbose:
            print("stegging "+ file+"."+ext+" in progess....")
            print("Maximum bytes to encode for "+ file+"."+ext+" is "+n_byte)
            print("\n")
>>>>>>> 7f57d6394d4f3c131e6b2c92a80cd28992c218f0
 
        
        #Generate secreat message
        randomString = generateRandomString(randomTextSize=randomTextSize)
        if len(randomString) > n_byte:
            raise ValueError("[!] Insufficient bytes, need bigger image or less data")


        outPutFileName = os.path.join(path,f"{file}_stegged.png")
        #stegging
        secret = stegano.lsb.hide(files,randomString)
        secret.save(outPutFileName)
        count = count + 1

#main function 
if __name__ == '__main__':
    import argparse as arg
    parser = arg.ArgumentParser(description="Bulk stegnography with random text image use.")
    parser.add_argument("-d","--dir",help="specify the directory location")
    parser.add_argument("-T","--text",help="Amount of random string to be genrated")
    #parser.add_argument("-e","--encode",help="encoding all the images")
    parser.add_argument("-a","--algorithm",help="specifiy the algorithm used (only LSB is avaiable right now)")
    parser.add_argument("-o","--output",help="specify the directory location for the output")
    parser.add_argument("-v","--verbos",help="Provide a detail verboss output")
    
    args = parser.parse_args()
    base_path = args.dir
    textSize = int(args.text)
    #get file information and total number of files based on directory location
    # variables used for the images information
    #allImageName= [f for f in os.listdir(base_path) if isfile(join(base_path,f))]
    #print(os.listdir(base_path))
    


    allImageName = []
    fileName = []
    for i in os.listdir(base_path):
        fileName.append(i)
        allImageName.append(join(base_path,i))

    #encoding images
    if args.verbos:
        verbose=True
    if args.output:
        #send image information (allImageName), path, size of random text, and location of the output steg
        encode(ImageName=allImageName,randomTextSize=textSize,outputLocation=args.output,Filename=fileName)
    else:
        raise ValueError("[!] Please provide output directory location")




    

