from http.server import HTTPServer, SimpleHTTPRequestHandler, test
import sys
import ssl
class CORSRequestHandler (SimpleHTTPRequestHandler):
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        SimpleHTTPRequestHandler.end_headers(self)
if __name__ == '__main__':
    httpd = HTTPServer(('localhost', 8000), CORSRequestHandler)
    # test(CORSRequestHandler, HTTPServer, port=int(sys.argv[1]) if len(sys.argv) > 1 else 8000)
    httpd.serve_forever()


