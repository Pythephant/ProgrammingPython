import os,sys
from http.server import HTTPServer, CGIHTTPRequestHandler	

webdir = '.'
port = 80

os.chdir(webdir)
serverAddress = ("",port)
serverObj = HTTPServer(serverAddress, CGIHTTPRequestHandler)
serverObj.serve_forever()
