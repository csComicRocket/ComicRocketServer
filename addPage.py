import sys, random, collections
import textGen
import pymysql
import png
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

    #find site ID
    cur.execute("SELECT id FROM sites WHERE class = 'XKCD'")
    for row in cur.fetchall():
        siteId, = row
        break

    #get last page
    cur.execute("SELECT * FROM pages WHERE site_id = {0} AND next_id IS NULL".format(siteId))
    for row in cur.fetchall():
        id, site_id, next_id, uri_path = row
        lastPage = {'id': id, 'site_id': site_id, 'next_id': next_id, 'uri_path': uri_path}
        break

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

    print("New Page (id:{0}) added to XKCD".format(newId))

if __name__ == '__main__':
    page = sys.argv[1]
    
    #connect to mysql
    conn = pymysql.connect(host='localhost', port=3306, user='ohmu', passwd='TGSTGSTGS', db='crts')
    cur = conn.cursor()

    for case in switch(page):
        if case('XKCD'):
            AddXKCD(cur)
            break
        if case():
            ''''''
            break
        #more cases here

    #close connections
    cur.close()
    conn.close()