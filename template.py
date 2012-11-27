# the base template

import comment
from string import Template

class TemplatePage:
    
    _values = {}                # key values to replace in the template text
    _template = None            # python template class
    _commentTemplate = None     # comment template class name 
    _comments = []              # list of comments

    def __init__(self, template, commentTemplate):
        # load template from file (ie raw html with predefiened key values)
        templateFile = open(template)
        self._template = Template(templateFile.read())
        templateFile.close()

        # save the comment template class
        self._commentTemplate = commentTemplate

    def __str__(self):
        self.SetValue('comments', self._BuildComments())
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

#http://www.xkcd.com/
class XKCDPage(TemplatePage):

    def __init__(self):
        # call base constructor
        TemplatePage.__init__(self, 'XKCD.html', None)

#http://www.penny-arcade.com/
class PennyArcade(TemplatePage):

    def __init__(self):
        # call base constructor
        TemplatePage.__init__(self, 'PennyArcade.html', None)

#http://www.sandraandwoo.com/
class SandraAndWoo(TemplatePage):

    def __init__(self):
        # call base constructor
        TemplatePage.__init__(self, 'SandraAndWoo.html', None)

#http://www.dilbert.com/

#http://www.explosm.net/comics/new/

#http://drmcninja.com/

#http://www.alessonislearned.com/



if __name__ == '__main__':
    test = XKCDPage()
    print(str(test))
    test = PennyArcade()
    print(str(test))