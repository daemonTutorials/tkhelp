import http.server
import socketserver

PORT = 8085
Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)
print("server listen at:",PORT)
httpd.serve_forever()
