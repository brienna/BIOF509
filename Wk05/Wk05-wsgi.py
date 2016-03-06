from wsgiref.simple_server import make_server


def simple_app(environ, start_response):
    """A simple WSGI application"""
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response(status, headers)

    return ["Hello World\n".encode('utf-8')]

if __name__ == '__main__':
    httpd = make_server('', 8000, simple_app)
    print("Serving on port 8000...")
    httpd.serve_forever()
