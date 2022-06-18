# py-image-server
A HTTP server which provides flexible image processing functionality.
The HTTP server is realized with fastAPI, running through uvicorn.
The image processing functionalities are implemented with opencv.

The user sends a request in JSON format through the API to the webserver.
The webserver picks up the request in a parallel process and processes the images.

## Request format
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
1. Resizing the image to any reasonable size smaller than the origin image.
2. Split the image into left-top/right-top/left-bottom/right-bottom sub-images and
process/store them separately
3. Blur the full image, for example by applying a Gaussian filter or by downsampling
followed by upsampling.
4. Any combination of the above operations

## Additional requirements
- Images should be saved to JPG and PNG images defined by the callers
- Images within a request should be processed concurrently/in-parallel.

## Software overview
The software consists of two main components:
1. A HTTP service that handles requests
2. Concurrent image processing

