
from string import Template

class Comment:

    _values = {}
    _template = None


    def __init__(self, template, username, timestamp, title, message):
        self._values['username'] = username
        self._values['timestamp'] = timestamp
        self._values['title'] = title
        self._values['message'] = message

        templateFile = open(template)
        self._template = Template(templateFile.read())
        templateFile.close()

    def __str__(self):
        return self._template.safe_substitute(self._values)

class XKCDComment(Comment):

    def __init__(self, username, timestamp, title, message):
        Comment.__init__(self, 'XKCDComment.html', username, timestamp, title, message)


if __name__ == '__main__':
    test = XKCDComment('ohmusama', '3 Nov 2012', 'No Comment', 'No seriously "No Comment"')
    print(str(test))
