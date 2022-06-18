# py-image-server
A HTTP server which provides flexible image processing functionality.
The HTTP server is realized with fastAPI, running through uvicorn.
The image processing functionalities are implemented with opencv.

The user sends a request in JSON format through the API to the webserver.
The webserver picks up the request in a parallel process and processes the images.
Images are stored locally on the server, and the request defines the paths on the server.

# [1] Design of the software

## Software overview
The software consists of two main components:
1. A webserver based on fastAPI that handles HTTP requests in JSON format in concurrent processes
2. An image processor that offers a variety of image modifications

## Server implementation
The webserver is based on the fastAPI package, and is run with Uvicorn.
The requests are defined using the fastAPI JSON format: 

    {
        images:     [{"input":"inputPath1","output":"outputPath1"},
                     {"input":"inputPath2","output":"outputPath2"},
                     ...
                     {"input":"inputPathN","output":"outputPathN"}],
        operations: ["operation1", 
                     "operation2",
                     ...
                     "operationN"]
    }


## Image processing functionalities
There are in total 3 different functionalities in the image processor, 
which can be called in any order defined in the request

1. Resizing the image to any reasonable size smaller than the origin image.
2. Split the image into left-top/right-top/left-bottom/right-bottom sub-images and
process/store them separately
3. Blur the full image, for example by applying a Gaussian filter or by downsampling
followed by upsampling.

The operations can be called through the following example
    
    "resize=scalingFactor", with scalingFactor=(0.05,100]
    "split=True"
    "blur=kernelSize", with kernelSize=[0,inf)

Here, the resizing scaling factor is a float that denotes the percentag scaling to be done.
If split in the operations list, it will work for any string besides "None", "false", or "False", which will skip splitting.
The blur kernelSize is an integer that indicates the Gaussian blur kernel size. If this is zero, the kernelSize will be computed automatically from Sigma (https://www.tutorialkart.com/opencv/python/opencv-python-gaussian-image-smoothing/).

# [2] Installation and first run

# [3] Extensive testing using automated pytests
