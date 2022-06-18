from typing import List
from pydantic import BaseModel
import os
import cv2

class Image(BaseModel):
    input: str
    output: str

class Request(BaseModel):
    images: List[Image] = []
    operations: List[str] | None = None

def ProcessRequest(request=Request):
    imageProcessors = []
    for image in request.images:
        processor = ImageProcessor(image)
        if processor.readImage():
            imageProcessors.append(processor)
    print("Initialized",len(imageProcessors),"processors.")
    for processor in imageProcessors:
        processor.performOperations(request.operations)
    print("Processed",len(imageProcessors),"images.")
    for processor in imageProcessors:
        processor.saveResults()

class ImageProcessor():
    def __init__(self, image):
        self.DEBUG_MODE = False
        self.inputPath = image.input
        self.outputPath = image.output
        self.outputFileName, self.outputFileFormat = self.getImageNameAndFormat(image.output)
        # Storing the image in a list in case we ever want to split the image
        self.images = []

    def performOperations(self, operations=None):
        if operations is None:
            operations = [str]
        self.debugImshow("Original",self.images[0])
        for item in operations:
            itemFields = item.split("=")
            method = itemFields[0]
            arguments = itemFields[1]
            print("Method:",method,"| arguments:",arguments)
            getattr(self, method)(arguments)
        if self.DEBUG_MODE:
            cv2.waitKey(0)

    def readImage(self):
        try:
            image = cv2.imread(self.inputPath)
            self.images.append(image)
            return True
        except:
            print("FAILED TO READ IMAGE:",self.inputPath)
            return False

    def getImageNameAndFormat(self,path):
        fileName, fileFormat = os.path.splitext(path)
        return fileName, fileFormat

    def resize(self, arguments=str):
        scaling = float(arguments)
        processedImages = []
        for img in self.images:
            width = int(img.shape[1] * scaling)
            height = int(img.shape[0] * scaling)
            dim = (width, height)
            processedImages.append(cv2.resize(img, dim, interpolation = cv2.INTER_AREA))
        self.images = processedImages
        print("Resized",len(self.images),"image(s) with scaling",scaling)
        self.debugImshow("Resizing",self.images[0])


    def splitQuadrants(self, arguments=str):
        processedImages = []
        for img in self.images:
            half_width = int(img.shape[0]/2)
            half_height = int(img.shape[1]/2)
            processedImages.append(img[:half_width,:half_height])
            processedImages.append(img[:half_width,half_height:])
            processedImages.append(img[half_width:,:half_height])
            processedImages.append(img[half_width:,half_height:])
        self.images = processedImages
        print("Split",len(self.images),"into",len(processedImages),"image(s)")
        self.debugImshow("Split quadrant",self.images[0])


    def blur(self, argument):
        blurFactor = int(argument)
        processedImages = []
        for img in self.images:
            processedImages.append(cv2.GaussianBlur(img,(blurFactor,blurFactor),cv2.BORDER_DEFAULT))
        self.images = processedImages
        print("Blurred",len(self.images),"image(s)")
        self.debugImshow("Blurred",processedImages[0])

    def saveResults(self):
        if len(self.images)==1:
            cv2.imwrite(self.outputPath, self.images[0])
        else:
            N = 1
            for img in self.images:
                cv2.imwrite("{}_{}{}".format(self.outputFileName,N,self.outputFileFormat), img)
                N += 1
        print("Saved image processing results")

    def exportPng(self):
        print("export png")

    def exportJpg(self):
        print("export jpg")

    def debugImshow(self, plotname,img):
        if self.DEBUG_MODE:
            cv2.imshow(plotname,img)

