#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import urlparse

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		self.send_response(200)
		qs = {}
		path = self.path
		if '?' in path:
			tmp = path.split('?')
			tmp[0] = tmp[0][1:]

		finalString = "Rates and all that shit"
		#self.wfile.write("longi: "+tmp[0]+"\nlati: " +tmp[1])


		#send_response(code[, message])
		self.send_header('Content-type','text/html')
		#self.send_header('Content', finalString) 
		self.end_headers()
		# Send the html message
		#print"Crime Ratesss"
		self.wfile.write("Crime rate:100%") 
		return

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()

#def crimeDataRetrieval():
