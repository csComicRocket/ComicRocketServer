import sys, random, collections
import textGen
import pymysql
import png
import platform
import time
from switch import switch

'''
PageRow = collections.namedtuple('pageRow', "id site_id next_id uri_path")
t = PageROw(*row)

t.id
t.site_id
t.next_id
t.uri_path
'''

def AddXKCD(cur):

    #check if it is the proper number of day updates. Each time this is run it is considered 1 day
    try:
        f = open('xkcd.day', 'r+')
        day = int(f.read())
        f.close()
    except Exception as e:
        f = open('xkcd.day', 'w')
        day = 0
        f.write(str(day))
        f.close()

    #increment day by 1
    f = open('xkcd.day', 'w')
    f.write(str((day+1)%7))
    f.close()

    if not (day in [1, 3, 5]):
        print('Day Skipped');
        return

    #find site ID
    cur.execute("SELECT id FROM sites WHERE class = 'XKCD'")
    for row in cur.fetchall():
        siteId, = row
        break

    #get last page
    cur.execute("SELECT * FROM pages WHERE site_id = {0} AND next_id IS NULL".format(siteId))
    firstPageExists = False
    for row in cur.fetchall():
        firstPageExists = True
        id, site_id, next_id, uri_path = row
        lastPage = {'id': id, 'site_id': site_id, 'next_id': next_id, 'uri_path': uri_path}
        break

    newId = None
    if firstPageExists:

        #build next page uri
        nextUri = '/' + str(int(lastPage['uri_path'][1:-1]) + 1) + '/'
        
        #insert new page
        cur.execute("INSERT INTO pages (site_id, uri_path) VALUES ({0}, '{1}')".format(siteId, nextUri))

        #find the new id
        cur.execute("SELECT LAST_INSERT_ID()")
        for row in cur.fetchall():
            newId, = row
            break

        #point next page to the new page
        cur.execute("UPDATE pages SET next_id = {0} WHERE id = {1}".format(newId, lastPage['id']))

    else:

        #make first uri
        firstUri = '/1/';

        #insert first page
        cur.execute("INSERT INTO pages (site_id, uri_path) VALUES({0}, '{1}')".format(siteId, firstUri))

        #find the new id
        cur.execute("SELECT LAST_INSERT_ID()")
        for row in cur.fetchall():
            newId, = row
            break

    ###

    #add variables for the new page

    #make the title
    title = textGen.BuildPhrase(random.randint(2,5), False).title()
    hover = textGen.BuildParagraph(random.randint(1,3))

    #add title
    cur.execute("INSERT INTO components (`key`, `value`) VALUES('{0}', '{1}')".format('title', title))
    #find the title id
    cur.execute("SELECT LAST_INSERT_ID()")
    for row in cur.fetchall():
        titleId, = row
        break

    #add hover
    cur.execute("INSERT INTO components (`key`, `value`) VALUES('{0}', '{1}')".format('hover', hover))
    #find the hover id
    cur.execute("SELECT LAST_INSERT_ID()")
    for row in cur.fetchall():
        hoverId, = row
        break

    #link the components to the page
    cur.execute("INSERT INTO page_components (page_id, component_id) VALUES({0}, {1}), ({0}, {2})".format(newId, titleId, hoverId))

    ###

    #generate lowercase title
    lowTitle = title.lower().replace(' ', '_')

    try:
        #create comic in appropriate spot
        f = open("webroot/www.xkcd.com/comics/{0}.png".format(lowTitle), 'wb')      # binary mode is important
        width = random.randint(248, 713)
        height = random.randint(217, 437)
        w = png.Writer(width, height)

        #build image noise
        lines = []
        for y in range(height):
            row = []
            for x in range(width):
                row.append(random.randint(0, 255))
                row.append(random.randint(0, 255))
                row.append(random.randint(0, 255))
            lines.append(row)

        #write lines to files
        w.write(f, lines)
        f.close()
    except Exception as e:
        print(e)

    print("New Page (id:{0}) added to XKCD".format(newId))

    path = 'www.xkcd.com.list' #this is the "domain" field in the database + '.list'

    #we are running on windows, use ./ as path
    if platform.system() == 'Windows':
        path = './' + path
    #we are running on server, use /usr/local/bin/ as path
    else :
        path = '/usr/local/bin/' + path

    try:
        f = open(path, 'a+')
        f.write("http://www.xkcd.com{0}\n".format(nextUri))
        f.close()
    except Exception as e:
        print(e)

def AddDoomsDayMyDear(cur):

    #check if it is the proper number of day updates. Each time this is run it is considered 1 day
    try:
        f = open('doomsdaymydear.day', 'r+')
        day = int(f.read())
        f.close()
    except Exception as e:
        f = open('doomsdaymydear.day', 'w')
        day = 0
        f.write(str(day))
        f.close()

    #increment day by 1
    f = open('doomsdaymydear.day', 'w')
    f.write(str((day+1)%7))
    f.close()

    if not (day in [1, 5]):
        print('Day Skipped');
        return

    #wait 0-4 hours (5sec = 1 hour for accelerated time)
    duration = random.random() * 4 * 5
    print("Waiting {0} seconds".format(duration))
    time.sleep(duration)

    #find site ID
    cur.execute("SELECT id FROM sites WHERE class = 'DoomsDayMyDear'")
    for row in cur.fetchall():
        siteId, = row
        break

    #get last page
    cur.execute("SELECT * FROM pages WHERE site_id = {0} AND next_id IS NULL".format(siteId))
    firstPageExists = False
    for row in cur.fetchall():
        firstPageExists = True
        id, site_id, next_id, uri_path = row
        lastPage = {'id': id, 'site_id': site_id, 'next_id': next_id, 'uri_path': uri_path}
        break

    #there is already a page
    if firstPageExists:

        #build next page uri
        print(lastPage)
        nextId = int(lastPage['uri_path'][5:]) + 1
        nextUri = '/?id=' + str(nextId)

        #insert new page
        cur.execute("INSERT INTO pages (site_id, uri_path) VALUES ({0}, '{1}')".format(siteId, nextUri))

        #find the new id
        cur.execute("SELECT LAST_INSERT_ID()")
        for row in cur.fetchall():
            newId, = row
            break

        #point next page to the new page
        cur.execute("UPDATE pages SET next_id = {0} WHERE id = {1}".format(newId, lastPage['id']))

    else:

        #make first uri
        nextId = 1
        firstUri = '/?id=1';

        #insert first page
        cur.execute("INSERT INTO pages (site_id, uri_path) VALUES({0}, '{1}')".format(siteId, firstUri))

        #find the new id
        cur.execute("SELECT LAST_INSERT_ID()")
        for row in cur.fetchall():
            newId, = row
            break

    ###

    #add variables for the new page

    #build news item
    cur.execute("SELECT MAX(value) FROM components WHERE `key` LIKE 'news_id'")
    for row in cur.fetchall():
        maxNewsId, = row
        if maxNewsId == None:
            maxNewsId = 0
        break

    news_title = textGen.BuildPhrase(random.randint(2, 5), False).title()
    news_content = textGen.BuildParagraph(random.randint(1,3))
    news_id = int(maxNewsId) + 1

    #add news title
    cur.execute("INSERT INTO components (`key`, `value`) VALUES('{0}', '{1}')".format('news_title', news_title))
    #find the title id
    cur.execute("SELECT LAST_INSERT_ID()")
    for row in cur.fetchall():
        titleId, = row
        break

    #add news content
    cur.execute("INSERT INTO components (`key`, `value`) VALUES('{0}', '{1}')".format('news_content', news_content))
    #find the hover id
    cur.execute("SELECT LAST_INSERT_ID()")
    for row in cur.fetchall():
        contentId, = row
        break
    
    #add news id
    cur.execute("INSERT INTO components (`key`, `value`) VALUES('{0}', '{1}')".format('news_id', news_id))
    #find the hover id
    cur.execute("SELECT LAST_INSERT_ID()")
    for row in cur.fetchall():
        newsId, = row
        break

    #link the components to the page
    cur.execute("INSERT INTO page_components (page_id, component_id) VALUES({0}, {1}), ({0}, {2}), ({0}, {3})".format(newId, titleId, contentId, newsId))



    ###

    #create comic in appropriate spot
    f = open("webroot/www.doomsdaymydear.com/img/comic/{0}.png".format(nextId), 'wb')      # binary mode is important
    width = 800
    height = 1140
    w = png.Writer(width, height)

    #build image noise
    lines = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(random.randint(0, 255))
            row.append(random.randint(0, 255))
            row.append(random.randint(0, 255))
        lines.append(row)

    #write lines to files
    w.write(f, lines)
    f.close()

    print("New Page (id:{0}) added to DoomsDayMyDear".format(newId))

    path = 'www.doomsdaymydear.com.list' #this is the "domain" field in the database + '.list'

    #we are running on windows, use ./ as path
    if platform.system() == 'Windows':
        path = './' + path
    #we are running on server, use /usr/local/bin/ as path
    else :
        path = '/usr/local/bin/' + path

    try:
        f = open(path, 'a+')
        f.write("http://www.doomsdaymydear.com/?id={0}\n".format(newId))
        f.close()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    site = sys.argv[1]
    
    #connect to mysql
    conn = pymysql.connect(host='localhost', port=3306, user='ohmu', passwd='TGSTGSTGS', db='crts')
    cur = conn.cursor()

    for case in switch(site):
        if case('XKCD'):
            AddXKCD(cur)
            break
        if case('DoomsDayMyDear'):
            AddDoomsDayMyDear(cur)
            break
        if case():
            print ("That site isn't recognized!")
            break
        #more cases here

    #close connections
    cur.close()
    conn.close()