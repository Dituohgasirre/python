#!/usr/bin/env python3


import http.server as hs


if __name__ == "__main__":
    def main():
        httpd = hs.HTTPServer(("", 6789), hs.SimpleHTTPRequestHandler)
        httpd.serve_forever()

    main()
