# py-image-server
A HTTP server which provides flexible image processing functionality.

## Request contents
1. list of jpg image paths
2. list of operations
3. list of output paths for each image

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

