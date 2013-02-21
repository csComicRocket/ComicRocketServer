
import pymysql
import platform


conn = pymysql.connect(host='localhost', port=3306, user='ohmu', passwd='TGSTGSTGS', db='crts')
cur = conn.cursor()

cur.execute("SELECT id, domain FROM sites")

comics = {}
for row in cur.fetchall():
    id, domain = row
    comics[domain] = id

try:
    path = 'comics.ids'
    
    #we are running on windows, use ./ as path
    if platform.system() == 'Windows':
        path = './' + path
    #we are running on server, use /usr/local/bin/ as path
    else :
        path = '/usr/local/bin/' + path

    f = open(path, 'w')
    f.write(str(comics))

except Exception as e:
    print(e)
