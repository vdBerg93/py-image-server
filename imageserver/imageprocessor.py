
# class Image():
#     def __init__(self, ):


class ImageProcessor():
    def __init__(self, request):
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
