
import pymysql
import png
import platform
import time
import sys
from switch import switch


def ListPages(cur, comicId, domain, pageParam):
    
    cur.execute("SELECT id FROM pages WHERE site_id={0}".format(comicId))

    path = domain + '.list' #this is the "domain" field in the database + '.list'

    #we are running on windows, use ./ as path
    if platform.system() == 'Windows':
        path = './' + path
    #we are running on server, use /usr/local/bin/ as path
    else :
        path = '/usr/local/bin/' + path


    try:
        f = open(path, 'w')
    
        for row in cur.fetchall():
            id, = row
            f.write(("http://" + domain + pageParam + "\n").format(id))

        #finally close file
        f.close()
    
    except Exception as e:
        print(e)


if __name__ == '__main__':
    site = sys.argv[1]
    
    #connect to mysql
    conn = pymysql.connect(host='localhost', port=3306, user='ohmu', passwd='TGSTGSTGS', db='crts')
    cur = conn.cursor()

    cur.execute("SELECT id, domain FROM sites WHERE class='{0}'".format(site))
    for row in cur.fetchall():
        id, domain = row
        break

    for case in switch(site):
        if case('XKCD'):
            ListPages(cur, id, domain, '/{0}/')
            break
        if case('DoomsDayMyDear'):
            ListPages(cur, id, domain, '/?id={0}')
            break
        if case():
            print ("That site isn't recognized!")
            break
        #more cases here

    #close connections
    cur.close()
    conn.close()