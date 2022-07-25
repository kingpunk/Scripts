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

from progress.bar import Bar
import os
from os.path import isfile,join
from PIL import Image
import cv2
import numpy as np
import itertools
import random
import re
import stegano
import string

verbose = False

def generateRandomString(randomTextSize):

    letters = string.ascii_lowercase + string.ascii_uppercase + string.ascii_letters #+ string.digits + string.punctuation
    
    text = ''.join(random.choice(letters) for i in range(randomTextSize))

    
    return text

#dct required function

# QUNTIZATION TABLE reuired for DCT

quant = np.array([[16,11,10,16,24,40,51,61],      
                    [12,12,14,19,26,58,60,55],
                    [14,13,16,24,40,57,69,56],
                    [14,17,22,29,51,87,80,62],
                    [18,22,37,56,68,109,103,77],
                    [24,35,55,64,81,104,113,92],
                    [49,64,78,87,103,121,120,101],
                    [72,92,95,98,112,100,103,99]])


def toBinary(hide_data):
    bits = []
    for char in hide_data:
        binval = bin(ord(char))[2:].rjust(8,'0')
        bits.append(binval)
    numberofBits = bin(len(bits))[2:].rjust(8,'0')
    return bits,numberofBits

def addPadd(img,row,col):
    img = cv2.resize(img,(col+(8-col%8),row+(8-row%8)))
    return img

def getRowCol(image):
    return image.shape[:2]


def chunks(changedImageValue,col):
    intergetColumnValue = int(col)
    for i in range(0,len(changedImageValue),intergetColumnValue):
        yield changedImageValue[i:i + intergetColumnValue]

# dct function end

###function for lsb random

def LstBit(source,target):
    ## Matching the last bit of binary
    replace_reg = re.compile(r'[1|0]$')  
    return replace_reg.sub(target,source)

def StringtoBin(string):
    #Convert a string to binary , Not enough 8 Bit complement 8 position
    return ''.join(bin(ord(c)).replace('0b','').rjust(8,'0') for c in string)



#lsb random function end




def encode(ImageName,randomTextSize,outputLocation,Filename):
    #get Filename, extension, path
    bar = Bar('Processing', max=len(ImageName))
    count = 0
    try:
        outputDirectory = "OutputSteggLSB"
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
        bar.next()
        print("stegging "+ file+"."+ext+" in progess....")
        #print("Maximum bytes to encode for "+ file+"."+ext+" is "+n_byte)

        #if verbose:
        #    print("stegging "+ file+"."+ext+" in progess....")
        #    print("Maximum bytes to encode for "+ file+"."+ext+" is "+n_byte)
        #    print("\n")

 
        
        #Generate secreat message
        randomString = generateRandomString(randomTextSize=randomTextSize)
        if len(randomString) > n_byte:
            raise ValueError("[!] Insufficient bytes, need bigger image or less data")


        outPutFileName = os.path.join(path,f"{file}_stegged.png")
        #stegging
        secret = stegano.lsb.hide(files,randomString)
        secret.save(outPutFileName)
        count = count + 1
    bar.finish()



def encodeLSBran(ImageName,randomTextSize,outputLocation,Filename):
    file_count = 0
    bar = Bar('Processing', max=len(ImageName))
    try:
        outputDirectory = "OutputSteggLSBRan"
        path=os.path.join(outputLocation,outputDirectory)
        os.mkdir(path)
    except:
        raise Exception("Something is wrong with Output file location")
    
    for files in ImageName:
        #file name
        file, ext = Filename[file_count].split(".")
        #get secret information
        data = generateRandomString(randomTextSize=randomTextSize)
        file_count = file_count+1
        data = StringtoBin(data)
        im = Image.open(files)
        width = im.size[0] # Width 
        height = im.size[1] # Height 
        count = 0
        if width*height<len(data):
            print(" Too much data ")
            return
        bar.next()
        print("stegging "+ file+"."+ext+" in progess....")
        for h in range(height):
            for w in range(width):
                # Get pixels 
                pixel = im.getpixel((w,h))
                # Take three channel values （ Decimal system ）
                R = pixel[0]
                G = pixel[1]
                B = pixel[2]
                # Decimal to binary 
                R_bit = bin(R).replace("0b","")
                G_bit = bin(G).replace("0b","")
                B_bit = bin(B).replace("0b","")
                # Randomly select a channel to store the last bit binary 
                choose = random.randint(0,2)
                if count==len(data): # When the data is saved 
                    break
                if choose==0: # stay R The last bit of the channel stores data 
                    R_bit = LstBit(R_bit,data[count])
                    count += 1
                if count==len(data): # When the data is saved 
                    break
                elif choose==1: # stay G The last bit of the channel stores data 
                    G_bit = LstBit(G_bit,data[count])
                    count += 1
                if count==len(data): # When the data is saved 
                    break
                elif choose==2: # stay B The last bit of the channel stores data 
                    B_bit = LstBit(B_bit,data[count])
                    count += 1
                if count==len(data): # When the data is saved 
                    break
                # Binary to decimal 
                R_bit = int(R_bit,2)
                G_bit = int(G_bit,2)
                B_bit = int(B_bit,2)
                # Write back pixels 
                im.putpixel((w,h),(R_bit,G_bit,B_bit))
                if count==len(data): # When the data is saved 
                    break
        outPutFileName = os.path.join(path,f"{file}_stegged.png")
        im.save(outPutFileName)
    bar.finish()
    

def encodeDCT(ImageName,randomTextSize,outputLocation,Filename):
    count = 0
    bar = Bar('Processing', max=len(ImageName))
    try:
        outputDirectory = "OutputSteggDCT"
        path=os.path.join(outputLocation,outputDirectory)
        os.mkdir(path)
    except:
        raise Exception("Something is wrong with Output file location")
    
    for files in ImageName:
        #file name
        file, ext = Filename[count].split(".")
        #get secret information
        seccret_message = generateRandomString(randomTextSize=randomTextSize)
        count = count+1
        image = cv2.imread(files,cv2.IMREAD_UNCHANGED)
        #get the size of the image
        
        row, col = getRowCol(image=image)
        if ((col/8)*(row/8)<len(seccret_message)):
            print("Message too large to encode in the image")
            return
        bar.next()
        print(" stegging "+ file+"."+ext+" in progess....")
        seccret_message = str(len(seccret_message))+'*'+seccret_message
        binary_secret_message,numberofBit = toBinary(seccret_message)

        #divisible by 8 x 8
        if row%8 != 0 or col%8 != 0:
            image = addPadd(img=image,row=row,col=col)
    
        row,col = getRowCol(image)

        #get the RGB channels

        B_Color_image,G_Color_image,R_Color_image = cv2.split(image)
    
        # message to hide in the blue channel, therfore it needs to be converted to float32 
        B_Color_image = np.float32(B_Color_image)

        # break the channel into 8 x 8 block
        imageblocks = [np.round(B_Color_image[j:j+8,i:i+8]-128) for(j,i) in itertools.product(range(0,row,8),range(0,col,8))]

        #Blocks  are run through DCT function

        dctBlocks = [np.round(cv2.dct(image_block)) for image_block in imageblocks]

        #Blocks then run through quantization table

        quantizedDCT = [np.round(dct_block/quant) for dct_block in dctBlocks]

        #set LSB in DC value corrensponding bit of message

        messIndex = 0
        letterIndex = 0 

        for quantizedBlock in quantizedDCT:
            # find a list significant bit in DC and replace with message bit
            DC = quantizedBlock[0][0]
            DC = np.uint8(DC)
            DC = np.unpackbits(DC)
            DC[7] = binary_secret_message[messIndex][letterIndex]
            DC = np.packbits(DC)
            DC = np.float32(DC)
            DC = DC - 255
            quantizedBlock[0][0] = DC
            letterIndex = letterIndex + 1

            if letterIndex == 8:
                letterIndex = 0
                messIndex = messIndex + 1
                if messIndex == len(seccret_message):
                    break
    
        #blocks run inversely though quantization table

        sImagBlocks = [quantizedBlock *quant+128 for quantizedBlock in quantizedDCT]

        #blocks run within inverse DCT
        #puts the new Image back together

        sImage = []

        # create the final image
        for chunkRowBlocks in chunks(changedImageValue=sImagBlocks,col=col/8):
            for rowBlockNum in range(8):
                for block in chunkRowBlocks:
                    sImage.extend(block[rowBlockNum])
    
        sImage = np.array(sImage).reshape(row,col)
        #convert type from float to unit8
        sImage = np.uint8(sImage)
        sImage = cv2.merge((sImage,G_Color_image,R_Color_image))

        outPutFileName = os.path.join(path,f"{file}_stegged.png")
        cv2.imwrite(outPutFileName,sImage)
    bar.finish()





#main function 
if __name__ == '__main__':
    import argparse as arg
    parser = arg.ArgumentParser(description="Bulk stegnography with random text image use.")
    parser.add_argument("-d","--dir",help="specify the directory location")
    parser.add_argument("-T","--text",help="Amount of random string to be genrated")
    parser.add_argument("-e","--encode",help="specify algorith between LSB, LSBRan, DCT")
    #parser.add_argument("-a","--algorithm",help="specifiy the algorithm used (only LSB is avaiable right now)")
    parser.add_argument("-o","--output",help="specify the directory location for the output")
    
    
    args = parser.parse_args()
    base_path = args.dir
    textSize = int(args.text)
    encodeMethod = args.encode
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
    if encodeMethod == 'LSB':
        #send image information (allImageName), path, size of random text, and location of the output steg
        encode(ImageName=allImageName,randomTextSize=textSize,outputLocation=args.output,Filename=fileName)
    elif encodeMethod == 'LSBRan':
        encodeLSBran(ImageName=allImageName,randomTextSize=textSize,outputLocation=args.output,Filename=fileName)
    elif encodeMethod == 'DCT':
        encodeDCT(ImageName=allImageName,randomTextSize=textSize,outputLocation=args.output,Filename=fileName)
    else:
        raise ValueError("[!] Please provide output directory location")




    

