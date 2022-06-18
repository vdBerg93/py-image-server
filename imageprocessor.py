import os
import time
from typing import List
import cv2
from pydantic import BaseModel

TESTING_CONCURRENCY = True

class Image(BaseModel):
    input: str
    output: str

class Request(BaseModel):
    images: List[Image] = []
    operations: List[str] | None = None

def ProcessRequest(request=Request):
    if TESTING_CONCURRENCY:
        print("In concurrency testing mode. Sleeping for 30 seconds...")
        time.sleep(30)
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
        self.TESTING_PLOTS = False
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
        if self.TESTING_PLOTS:
            cv2.waitKey(0)

    def readImage(self):
        if os.path.isfile(self.inputPath):
            image = cv2.imread(self.inputPath)
            if image is not None:
                self.images.append(image)
                return True
            else:
                print("Failed to read image from file:",self.inputPath)
                return False
        else:
            print("File doesnt exist:",self.inputPath)
            return False

    def getImageNameAndFormat(self,path):
        fileName, fileFormat = os.path.splitext(path)
        return fileName, fileFormat

    def resize(self, arguments=str):
        scaling = float(arguments)
        if scaling<0.05 or scaling >= 100:
            print("Resize scaling factor",scaling,"out of bounds [0.05,100]. Skipping operation")
            return
        processedImages = []
        for img in self.images:
            width = int(img.shape[1] * scaling)
            height = int(img.shape[0] * scaling)
            dim = (width, height)
            processedImages.append(cv2.resize(img, dim, interpolation = cv2.INTER_AREA))
        self.images = processedImages
        print("Resized",len(self.images),"image(s) with scaling",scaling)
        self.debugImshow("Resizing",self.images[0])


    def splitQuadrants(self, argument=str):
        if argument == "None" or argument.lower() == "false":
            print("Split argument is",argument,". Skipping quadrant splitting.")
            return
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
        kernelSize = int(argument)
        if kernelSize < 0:
            print("Guassian blur kernel size (",kernelSize,") should be >=0. Skipping blur.")
            return
        processedImages = []
        for img in self.images:
            processedImages.append(cv2.GaussianBlur(img,(kernelSize,kernelSize),cv2.BORDER_DEFAULT))
        self.images = processedImages
        print("Blurred",len(self.images),"image(s)")
        self.debugImshow("Blurred",processedImages[0])

    def saveResults(self):
        folder = os.path.dirname(self.outputPath)
        if not os.path.exists(folder):
            os.mkdir(folder)
        if len(self.images)==1:
            cv2.imwrite(self.outputPath, self.images[0])
        else:
            N = 1
            for img in self.images:
                cv2.imwrite("{}_{}{}".format(self.outputFileName,N,self.outputFileFormat), img)
                N += 1
        print("Saved image processing results")

    def debugImshow(self, plotname,img):
        if self.TESTING_PLOTS:
            cv2.imshow(plotname,img)

