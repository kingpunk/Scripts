import os
import cv2
import sys
import math
import numpy as np
import itertools
import matplotlib.pyplot as plt
from PIL import Image
from pathlib import Path

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



def encodeDCT(imagepath,seccret_message,outputFilelocation):

    image = cv2.imread(imagepath,cv2.IMREAD_UNCHANGED)
    #get the size of the image
    row, col = getRowCol(image=image)

    if ((col/8)*(row/8)<len(seccret_message)):
        print("Message too large to encode in the image")
        return
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
    cv2.imwrite(outputFilelocation,sImage)


def decodeDCT(stegPath):
    image = cv2.imread(stegPath,cv2.IMREAD_UNCHANGED)
    row,col = getRowCol(image)
    messageSize=None
    messageBits = []
    buff = 0

    #split the image into RGB color channel

    B_color_image,G_color_image,R_color_image = cv2.split(image)

    #since message is hiden in blue channel, converting all float32 for dct function

    B_color_image = np.float32(B_color_image)

    #break the image into 8 X 8 blocks

    imgBlocks = [B_color_image[j:j+8 ,i:i+8]-128 for (j,i) in itertools.product(range(0,row,8),range(0,col,8))]

    #blocks run thoguh quntization table

    quantizedDCT = [img_Block/quant for img_Block in imgBlocks]
    i=0

    #message extracted from list significant bit of DC coff

    for quantizedBlock in quantizedDCT:
        DC = quantizedBlock[0][0]
        DC = np.uint8(DC)
        DC = np.unpackbits(DC)

        if DC[7] == 1:
            buff += (0 & 1) << (7 - i)
        elif DC[7] ==0:
            buff += (1 & 1) << (7 - i)
        
        i = i + 1

        if i == 8:
            messageBits.append(chr(buff))
            buff = 0
            i = 0
            if messageBits[-1] == '*' and messageSize is None:
                try:
                    messageSize = int(''.join(messageBits[:-1]))
                except:
                    pass
        
        if len(messageBits) - len(str(messageSize)) - 1 == messageSize:
            return ''.join(messageBits)[len(str(messageSize))+1:]

    sImage = []
    sImagBlocks = [quantizedBlock *quant+128 for quantizedBlock in quantizedDCT]
    # create the final image
    for chunkRowBlocks in chunks(changedImageValue=sImagBlocks,col=col/8):
        for rowBlockNum in range(8):
            for block in chunkRowBlocks:
                sImage.extend(block[rowBlockNum])
    
    sImage = np.array(sImage).reshape(row,col)
    #convert type from float to unit8
    sImage = np.uint8(sImage)
    sImage = cv2.merge((sImage,G_color_image,R_color_image))   
    return ''


if __name__=='__main__':
    imagePath = "C:\\Users\\pskavalekar\\Desktop\\DATASET\\\CapturedDataset\\NORMAL\\cap (1).jpg"
    newPath = "C:\\Users\\pskavalekar\\Desktop\\DATASET\\CapturedDataset\\stegDCT.png"
    data = "sdfhsjhglsjfsljfksdjfkhbgkuhfksddbfksdhuwhfwnkbfksfusdhfksddbkhuifhsdnksbshsfusnksajbdfksagfiahfskjdbvsabfsdsdf"+"sdfhsjhglsjfsljfksdjfkhbgkuhfksddbfksdhuwhfwnkbfksfusdhfksddbkhuifhsdnksbshsfusnksajbdfksagfiahfskjdbvsabfsdsdf"+"sdfhsjhglsjfsljfksdjfkhbgkuhfksddbfksdhuwhfwnkbfksfusdhfksddbkhuifhsdnksbshsfusnksajbdfksagfiahfskjdbvsabfsdsdf"
    #encodeDCT(imagepath=imagePath,seccret_message=data,outputFilelocation=newPath)
    stegText=decodeDCT(stegPath=newPath)
    if data == stegText:
        print("works")