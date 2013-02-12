import sys, collections
import pymysql
from switch import switch

if __name__ == '__main__':
    site = sys.argv[1]
    
    #connect to mysql
    conn = pymysql.connect(host='localhost', port=3306, user='ohmu', passwd='TGSTGSTGS', db='crts')
    cur = conn.cursor()

    #find site
    cur.execute("SELECT id FROM sites WHERE class = '{0}'".format(site))
    for row in cur.fetchall():
        siteId, = row
        break

    #find all associated pages
    pageIds = []
    cur.execute("SELECT id from pages WHERE site_id = {0}".format(siteId))
    for row in cur.fetchall():
        pageId, = row
        pageIds.append(str(pageId))

    pageIdStr = ', '.join(pageIds)

    #find all related components for all pages for site
    compIds = []
    cur.execute("SELECT component_id FROM page_components WHERE page_id IN({0})".format(pageIdStr))
    for row in cur.fetchall():
        compId, = row
        compIds.append(str(compId))

    compIdStr = ', '.join(compIds)

    #delete all compoenents and their relations
    if len(compIds) > 1:
        cur.execute("DELETE FROM components WHERE id IN({0})".format(compIdStr))
    if len(pageIds) > 1:
        cur.execute("DELETE FROM page_components WHERE page_id IN({0})".format(pageIdStr))

    #delete all comments
    if len(pageIds) > 1:
        cur.execute("DELETE FROM comments WHERE page_id IN({0})".format(pageIdStr))

    #delete all pages
    cur.execute("DELETE FROM pages WHERE site_id = {0}".format(siteId))

    #close connections
    cur.close()
    conn.close()