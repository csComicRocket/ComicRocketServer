import string, cgi, time, os
import pymysql
import template
from http import server

class MyRequestHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            host = self.headers['Host'].split(':')[0]
            print(self.headers['Host'], host, self.path)
            found = False

            conn = pymysql.connect(host='localhost', port=3306, user='ohmu', passwd='TGSTGSTGS', db='crts')
            cur = conn.cursor()

            cur.execute("SELECT * FROM sites WHERE domain LIKE '%{0}%'".format(host))

            for row in cur.fetchall():
                siteId, className, domain, filePath = row
                found = True
                break

            #find host in DB

            if found:

                #instantiate class
                _class = getattr(template, className)
                instance = _class(self.path)

                if instance.IsValid():
                    #build headers
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    
                    #write out the file loaded from the script
                    self.wfile.write(bytes(str(instance), 'UTF-8'))
                else:
                    #find path
                    try:
                        print("looking for file: webroot/{0}{1}".format(host, self.path))
                        f = open('webroot/{0}{1}'.format(host, self.path), 'rb')
                        self.wfile.write(f.read())
                    except IOError as e:
                        self.send_error(404, 'File Not Found %s' % self.path)

                return

            else:
                #look for path
                try:
                    print("looking for file: webroot/{0}{1}".format(host, self.path))
                    f = open('webroot/{0}{1}'.format(host, self.path), 'rb')
                    self.wfile.write(f.read())
                except IOError as e:
                    self.send_error(404, 'File Not Found %s' % self.path)

                #if no path, fail                
                self.send_error(404, 'File Not Found %s' % self.path)

            cur.close()
            conn.close()
         
        except Exception as e:
            print(e)
            self.send_error(500, 'Internal Server Error')
             
    def do_POST(self):
        self.do_GET() # currently same as post, but can be anything
         
def main():
    try:
        # you can specify any port you want by changing <q>80</q>
        HttpServer = server.HTTPServer(('', 80), MyRequestHandler) 
        print ('starting httpserver...')
        HttpServer.serve_forever()
    except KeyboardInterrupt:
        print ('^C received, shutting down server...')
        HttpServer.socket.close()
         
if __name__ == '__main__':
    main()