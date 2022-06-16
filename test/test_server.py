import urllib.request

# def test_server_request():
#     contents = urllib.request.urlopen("http://localhost:8888/test")

def test_single_image():
    images = "testimages/cyclo1.jpg"
    outputs = "testimages/cyclo1_processed.jpg"
    operations = "resize=[500,500],blur=0.5,split=[2,2]"
    path = "inputs:[{}]&outputs:[{}]&operations:[{}]".format(images, outputs, operations)
    contents = urllib.request.urlopen("http://localhost:8888/"+path)
    print(contents)
