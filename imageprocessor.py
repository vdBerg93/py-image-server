from pydantic import BaseModel

def ProcessRequest(request):
    images = []
    # for i
    # images.append(Image())

class Image(BaseModel):
    input: str
    output: str


class ImageProcessor():
    def __init__(self, inputPath, outputPath):
        print(request)
        print("running processor")
        raise NotImplementedError

    def ResizeImage(self):
        raise NotImplementedError

    def SplitQuadrants(self):
        raise NotImplementedError

    def BlurImage(self):
        raise NotImplementedError

    def ExportPng(self):
        raise NotImplementedError

    def ExportJpg(self):
        raise NotImplementedError
