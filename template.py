# the base template

import pymysql
import comment
from string import Template

class TemplatePage:
    
    _values = {}                # key values to replace in the template text
    _template = None            # python template class
    _commentTemplate = None     # comment template class name 
    _comments = []              # list of comments
    _valid = True

    def __init__(self, path, template, commentTemplate):
        # load template from file (ie raw html with predefiened key values)
        templateFile = open(path + '/' + template)
        self._template = Template(templateFile.read())
        templateFile.close()

        # save the comment template class
        self._commentTemplate = commentTemplate

    def __str__(self):
        self.SetValue('comments', self._BuildComments())
        print(self._values)
        return self._template.safe_substitute(self._values)

    def _BuildComments(self):
        commentHtml = ""
        for comment in self._comments:
            commentHtml += str(comment)

        return commentHtml

    def SetValue(self, key, value):
        self._values[key] = value;

    def ClearValue(self, key, value):
        del(self._values[key])

    def AddComment(self, username, timestamp, title, message):
        if not (_commentTemplate == None):
            commentClass = getattr(comment, _commentTemplate)
            instance = commentClass(username, timestamp, title, message)

    def IsValid(self):
        return self._valid

#http://www.xkcd.com/
class XKCD(TemplatePage):

    def __init__(self, uriPath):

        # call base constructor
        TemplatePage.__init__(self, 'XKCD', 'XKCD.html', None)

        #connect to mysql
        conn = pymysql.connect(host='localhost', port=3306, user='ohmu', passwd='TGSTGSTGS', db='crts')
        cur = conn.cursor()

        #find site ID
        cur.execute("SELECT id FROM sites WHERE class = 'XKCD'")
        for row in cur.fetchall():
            siteId, = row
            break

        #find page ID from uri
        siteFound = False
        cur.execute("SELECT id FROM pages WHERE site_id = {0} AND uri_path = '{1}'".format(siteId, uriPath))
        for row in cur.fetchall():
            pageId, = row
            siteFound = True
            break

        #check if on homepage, if so, page ID will be the most recent page
        if uriPath == '/':
            cur.execute("SELECT id FROM pages WHERE site_id = {0} AND next_id IS NULL".format(siteId))
            for row in cur.fetchall():
                pageId, = row
                siteFound = True

        #error if still no site is found
        if not siteFound:
            self._valid = False
            return

        #get first page
        cur.execute("SELECT * FROM pages p1 WHERE p1.site_id = {0} AND p1.id NOT IN(SELECT p2.next_id FROM pages p2 WHERE p2.next_id IS NOT NULL AND p2.site_id = {0})".format(siteId))
        print(str(cur))
        for row in cur.fetchall():
            id, page_id, next_id, uri_path = row
            firstPage = {'id': id, 'page_id': page_id, 'next_id': next_id, 'uri_path': uri_path}
            break

        #get previous page
        cur.execute("SELECT * FROM pages WHERE next_id = {0}".format(pageId))
        for row in cur.fetchall():
            id, page_id, next_id, uri_path = row
            previousPage = {'id': id, 'page_id': page_id, 'next_id': next_id, 'uri_path': uri_path}
            break

        #get current page
        cur.execute("SELECT * FROM pages WHERE id = {0}".format(pageId))
        for row in cur.fetchall():
            id, page_id, next_id, uri_path = row
            currentPage = {'id': id, 'page_id': page_id, 'next_id': next_id, 'uri_path': uri_path}
            break

        #get next page
        cur.execute("SELECT * FROM pages p1 WHERE p1.id = (SELECT p2.next_id FROM pages p2 WHERE id = {0})".format(pageId))
        for row in cur.fetchall():
            id, page_id, next_id, uri_path = row
            nextPage = {'id': id, 'page_id': page_id, 'next_id': next_id, 'uri_path': uri_path}
            break

        #get last page
        cur.execute("SELECT * FROM pages WHERE site_id = {0} AND next_id IS NULL".format(siteId))
        for row in cur.fetchall():
            id, page_id, next_id, uri_path = row
            lastPage = {'id': id, 'page_id': page_id, 'next_id': next_id, 'uri_path': uri_path}
            break

        ###

        #build vars

        #previous
        if currentPage['id'] != firstPage['id']:
            self.SetValue('prev', previousPage['uri_path'])
        else:
            self.SetValue('prev', '#')

        #current
        self.SetValue('current', currentPage['uri_path'])

        #next
        if currentPage['id'] != lastPage['id']:
            self.SetValue('next', nextPage['uri_path'])
        else:
            self.SetValue('next', '#')

        #get site vars
        cur.execute("SELECT c.key, c.value FROM components c JOIN site_components sc ON c.id = sc.component_id WHERE sc.site_id = {0}".format(siteId))
        for row in cur.fetchall():
            key, value = row
            self.SetValue(key, value)

        #get page vars
        cur.execute("SELECT c.key, c.value FROM components c JOIN page_components pc ON c.id = pc.component_id WHERE pc.page_id = {0}".format(pageId))
        for row in cur.fetchall():
            key, value = row
            self.SetValue(key, value)

            if key == 'title':
                titleLower = value.lower().replace(' ', '_')
                self.SetValue('title_lower', titleLower)

        cur.close()
        conn.close()

if __name__ == '__main__':
    test = XKCD(1)
    print(str(test))