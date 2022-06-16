import unittest
from http.server import ThreadingHTTPServer
from imageserver.server import MyServer

import urllib.request

class TestHttpServer(unittest.TestCase):
    def test_server(self):
        contents = urllib.request.urlopen("http://localhost:8888/test")
        print(contents)
