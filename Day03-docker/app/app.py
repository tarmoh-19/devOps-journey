from http.server import HTTPServer, BaseHTTPRequestHandler


class App(BaseHTTPRequestHandler):

    def do_GET(self):

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(b"""
        <html>
            <head>
                <title>DevOps Journey</title>
            </head>

            <body>
                <h1> Docker is Working!</h1>
                <h2>Day 3 DevOps Challenge</h2>

                <p>Hello Sebastian!</p>

                <p>This application is running inside a Docker container.</p>

            </body>
        </html>
        """)


server = HTTPServer(("0.0.0.0", 8000), App)

print("Server started on port 8000")

server.serve_forever()