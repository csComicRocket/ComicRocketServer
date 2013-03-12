import sys, random, collections
import textGen
import pymysql
import png
import platform
import time
from switch import switch
## run from cron (probably)

# add comments to existing pages, with probability frequency
# based on how fresh the page is
def AddXKCD(cur):
    pass

def AddDoomsDayMyDear(cur):
    
    #find site ID
    cur.execute("SELECT id FROM sites WHERE class = 'DoomsDayMyDear'")
    for row in cur.fetchall():
        siteId, = row
        break

    #get last page
    cur.execute("SELECT * FROM pages WHERE site_id = {0} AND next_id IS NULL".format(siteId))
    nextPageExists = False
    for row in cur.fetchall():
        nextPageExists = True
        id, site_id, next_id, uri_path = row
        page = {'id': id, 'site_id': site_id, 'next_id': next_id, 'uri_path': uri_path}
        break

    #loop until coment is added or we reach end of pages
    commentAdded = False 
    while not commentAdded and nextPageExists:
        #we stop here at this page, otherwise we delve deeper
        if random.randint(0, 1) == 1:
            username = textGen.BuildWord(random.randint(6,16))
            title = textGen.BuildPhrase(random.randint(1,5), False)
            message = textGen.BuildParagraph(random.randint(1,5))

            execution_text = "INSERT INTO comments (`page_id`, `datetime`, `username`, `title`, `body`, `avatar`) VALUES('{0}', NOW(), '{1}', '{2}', '{3}', '')".format(page['id'], username, title, message)
            print(execution_text) 
            
            cur.execute("INSERT INTO comments (`page_id`, `datetime`, `username`, `title`, `body`, `avatar`) VALUES('{0}', NOW(), '{1}', '{2}', '{3}', '')".format(page['id'], username, title, message))
            commentAdded = True

        #we get the next oldest page
        else :
            cur.execute("SELECT * FROM pages WHERE site_id = {0} AND next_id = {1}".format(siteId, page['id']))
            nextPageExists = False
            for row in cur.fetchall():
                nextPageExists = True
                id, site_id, next_id, uri_path = row
                page = {'id': id, 'site_id': site_id, 'next_id': next_id, 'uri_path': uri_path}
                break

    if commentAdded:
        print("Comment added to page_id:{0}".format(page['id']))
    else:
        print("Comment not added")

    return

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