import string, cgi, time, os
import pymysql
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
                id, className, domain, filePath = row
                #_class = getattr(FakeTemplates, className)
                #instance = _class()
                #print(instance)
                found = True
                break

            cur.close()
            conn.close()
            #find host in DB

            if found:

                #instantiate class

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(bytes(className, 'UTF-8'))
                #rs = os.popen('python /pathToFile/yourScript.py &')
                return

            else:
                self.send_error(404, 'File Not Found %s' % self.path)
         
        except Exception as e:
            print(e)
            self.send_error(500, 'Internal Server Error')
             
    def do_POST(self):
        self.do_GET() # currently same as post, but can be anything
         
def main():
    try:
        # you can specify any port you want by changing <q>81</q>
        HttpServer = server.HTTPServer(('', 81), MyRequestHandler) 
        print ('starting httpserver...')
        HttpServer.serve_forever()
    except KeyboardInterrupt:
        print ('^C received, shutting down server...')
        HttpServer.socket.close()
         
if __name__ == '__main__':
    main()