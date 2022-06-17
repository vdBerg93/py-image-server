from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from multiprocessing import Process
from oldserver import ImageProcessor

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Request:",self.path)
        processPath(self.path)
        p_new = Process(target=ImageProcessor, args=(self.path))
        print(p_new)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

def processPath(pathString):
    fields = pathString[1:].split("&")
    inputPaths = []
    outputPaths = []
    commands = []
    for command in fields:
        commandFields = command.split(":")
        what = commandFields[0]
        arguments = commandFields[1][1:-1]
        if what=="inputs":
            processInputs(arguments)
        elif what=="outputs":
            processOutputs(arguments)
        elif what=="operations":
            processOperations(arguments)
        else:
            raise NotImplementedError

def processInputs(arguments):
    print("Processing inputs:",arguments)
    # raise NotImplementedError

def processOutputs(arguments):
    print("Processing outputs:",arguments)
    # raise NotImplementedError

def processOperations(arguments):
    print("processing operations:",arguments)
    # raise NotImplementedError


if __name__ == "__main__":
    hostName = "localhost"
    serverPort = 8888

    webServer = ThreadingHTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
