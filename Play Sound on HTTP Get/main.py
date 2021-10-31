# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
from playsound import playsound
import threading

hostName = "0.0.0.0"
serverPort = 8080

def sound():
    playsound("sound.mp3")


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("Playing sound...", "utf-8"))

        thread = threading.Thread(target=sound)
        thread.start()

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")