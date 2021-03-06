# the base template

import pymysql
import comment
from string import Template

class TemplatePage:
    
    _values = None              # key values to replace in the template text
    _template = None            # python template class
    _commentTemplate = None     # comment template class name 
    _comments = []              # list of comments
    _valid = True               # is set to false if something bad happens
    _conn = None                # database connection
    _cur = None                 # database cursor
    siteId = 0                  # the id of the site, loaded from the db
    pageId = 0                  # the id of the currently loaded page

    def __init__(self, path, template, commentTemplate):
        self._values = {}

        # load template from file (ie raw html with predefiened key values)
        templateFile = open(path + '/' + template)
        self._template = Template(templateFile.read())
        templateFile.close()

        # save the comment template class
        self._commentTemplate = commentTemplate

        #connect to the database
        self._conn = pymysql.connect(host='localhost', port=3306, user='ohmu', passwd='TGSTGSTGS', db='crts')
        self._cur = self._conn.cursor()

        #find site ID
        self._cur.execute("SELECT id FROM sites WHERE class = '{0}'".format(path))
        for row in self._cur.fetchall():
            self.siteId, = row
            break

    #enter and exit will safely clean up db
    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):

        #clear db connections
        if not (self._cur == None):
            self._cur.close()
        if not (self._conn == None):
            self._conn.close()

    def __str__(self):
        self.SetValue('comments', self._BuildComments())
        subText = self._template.safe_substitute(self._values)
        while subText != self._template.template:
            self._template = Template(subText)
            subText = self._template.safe_substitute(self._values)
        return subText

    def _BuildComments(self):
        
        #build each comment
        self._comments = []
        self._cur.execute("SELECT * FROM comments WHERE page_id = {0}".format(self.pageId))
        for row in self._cur.fetchall():
            commentId, pageId, timeStamp, username, title, body, avatar = row
            self._comments.append(self._commentTemplate(username, timeStamp, title, body, avatar))

        #concatonate comments
        commentHtml = ""
        for comment in self._comments:
            commentHtml += str(comment)

        return commentHtml

    def GetPages(self, uriPath):
        
        #find page ID from uri
        siteFound = False
        self._cur.execute("SELECT id FROM pages WHERE site_id = {0} AND uri_path = '{1}'".format(self.siteId, uriPath))
        for row in self._cur.fetchall():
            self.pageId, = row
            siteFound = True
            break

        #check if on homepage, if so, page ID will be the most recent page
        if uriPath == '/':
            self._cur.execute("SELECT id FROM pages WHERE site_id = {0} AND next_id IS NULL".format(self.siteId))
            for row in self._cur.fetchall():
                self.pageId, = row
                siteFound = True

        #error if still no site is found
        if not siteFound:
            #print(uriPath)
            #print("Site Not Found!")
            self._valid = False
            return False

        pages = {}

        #get first page
        self._cur.execute("SELECT * FROM pages p1 WHERE p1.site_id = {0} AND p1.id NOT IN(SELECT p2.next_id FROM pages p2 WHERE p2.next_id IS NOT NULL AND p2.site_id = {0})".format(self.siteId))
        for row in self._cur.fetchall():
            id, site_id, next_id, uri_path = row
            pages['firstPage'] = {'id': id, 'site_id': site_id, 'next_id': next_id, 'uri_path': uri_path}
            break

        #get previous page
        self._cur.execute("SELECT * FROM pages WHERE next_id = {0}".format(self.pageId))
        for row in self._cur.fetchall():
            id, site_id, next_id, uri_path = row
            pages['previousPage'] = {'id': id, 'site_id': site_id, 'next_id': next_id, 'uri_path': uri_path}
            break

        #get current page
        self._cur.execute("SELECT * FROM pages WHERE id = {0}".format(self.pageId))
        for row in self._cur.fetchall():
            id, site_id, next_id, uri_path = row
            pages['currentPage'] = {'id': id, 'site_id': site_id, 'next_id': next_id, 'uri_path': uri_path}
            break

        #get next page
        self._cur.execute("SELECT * FROM pages p1 WHERE p1.id = (SELECT p2.next_id FROM pages p2 WHERE id = {0})".format(self.pageId))
        for row in self._cur.fetchall():
            id, site_id, next_id, uri_path = row
            pages['nextPage'] = {'id': id, 'site_id': site_id, 'next_id': next_id, 'uri_path': uri_path}
            break

        #get last page
        self._cur.execute("SELECT * FROM pages WHERE site_id = {0} AND next_id IS NULL".format(self.siteId))
        for row in self._cur.fetchall():
            id, site_id, next_id, uri_path = row
            pages['lastPage'] = {'id': id, 'site_id': site_id, 'next_id': next_id, 'uri_path': uri_path}
            break
    
        return pages

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

        #get the pages (first, prev, current, next, last)
        pages = self.GetPages(uriPath)

        if pages == False:
            return #error

        #build vars

        #previous
        if pages['currentPage']['id'] != pages['firstPage']['id']:
            self.SetValue('prev', pages['previousPage']['uri_path'])
        else:
            self.SetValue('prev', '#')

        #current
        self.SetValue('current', pages['currentPage']['uri_path'])

        #next
        if pages['currentPage']['id'] != pages['lastPage']['id']:
            self.SetValue('next', pages['nextPage']['uri_path'])
        else:
            self.SetValue('next', '#')

        #get site vars
        self._cur.execute("SELECT c.key, c.value FROM components c JOIN site_components sc ON c.id = sc.component_id WHERE sc.site_id = {0}".format(self.siteId))
        for row in self._cur.fetchall():
            key, value = row
            self.SetValue(key, value)

        #get page vars
        self._cur.execute("SELECT c.key, c.value FROM components c JOIN page_components pc ON c.id = pc.component_id WHERE pc.page_id = {0}".format(self.pageId))
        for row in self._cur.fetchall():
            key, value = row
            self.SetValue(key, value)

            if key == 'title':
                titleLower = value.lower().replace(' ', '_')
                self.SetValue('title_lower', titleLower)

        return

class DoomsDayMyDear(TemplatePage):

    def __init__(self, uriPath):
        # call base constructor
        TemplatePage.__init__(self, 'DoomsDayMyDear', 'DoomsDayMyDear.html', getattr(comment, 'DoomsDayMyDearComment'))

        #get the pages (first, prev, current, next, last)
        pages = self.GetPages(uriPath)

        if pages == False:
            return #error

        #build vars
        self.SetValue('id', pages['currentPage']['uri_path'][5:])

        #previous
        if pages['currentPage']['id'] != pages['firstPage']['id']:
            self.SetValue('first_link', '<a href="http://www.doomsdaymydear.com{0}"><img src="http://www.doomsdaymydear.com/img/first.png"></a>'.format(pages['firstPage']['uri_path'],))
            self.SetValue('prev_link', '<a href="http://www.doomsdaymydear.com{0}"><img src="http://www.doomsdaymydear.com/img/prev.png"></a>'.format(pages['previousPage']['uri_path']))
        else:
            self.SetValue('first_link', '')
            self.SetValue('prev_link', '')

        #current
        self.SetValue('current_link', pages['currentPage']['uri_path'])

        #next
        if pages['currentPage']['id'] != pages['lastPage']['id']:
            self.SetValue('next_link', '<a href="http://www.doomsdaymydear.com{0}"><img src="http://www.doomsdaymydear.com/img/next.png"></a>'.format(pages['nextPage']['uri_path']))
            self.SetValue('last_link', '<a href="http://www.doomsdaymydear.com{0}"><img src="http://www.doomsdaymydear.com/img/last.png"></a>'.format(pages['lastPage']['uri_path']))
        else:
            self.SetValue('next_link', '')
            self.SetValue('last_link', '')

        #get site vars
        self._cur.execute("SELECT c.key, c.value FROM components c JOIN site_components sc ON c.id = sc.component_id WHERE sc.site_id = {0}".format(self.siteId))
        for row in self._cur.fetchall():
            key, value = row
            self.SetValue(key, value)

        #get page vars
        self._cur.execute("SELECT c.key, c.value FROM components c JOIN page_components pc ON c.id = pc.component_id WHERE pc.page_id = {0}".format(self.pageId))
        for row in self._cur.fetchall():
            key, value = row
            self.SetValue(key, value)

        return


if __name__ == '__main__':
    test = XKCD(1)
    print(str(test))