# Python 3 server example
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from multiprocessing import Process
from imageprocessor import ImageProcessor

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Request:",self.path)
        p_new = Process(target=ImageProcessor, args=(self.path))
        print(p_new)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

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
