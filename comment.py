
from string import Template

class Comment:

    _values = None
    _template = None


    def __init__(self, template, username, timestamp, title, message, avatar):
        self._values = {}
        self._values['username'] = username
        self._values['timestamp'] = timestamp
        self._values['title'] = title
        self._values['message'] = message
        self._values['avatar'] = avatar

        templateFile = open(template)
        self._template = Template(templateFile.read())
        templateFile.close()

    def __str__(self):
        return self._template.safe_substitute(self._values)

class DoomsDayMyDearComment(Comment):

    def __init__(self, username, timestamp, title, message, avatar):
        Comment.__init__(self, 'DoomsDayMyDear/DoomsDayMyDearComment.html', username, timestamp, title, message, avatar)


if __name__ == '__main__':
    test = DoomsDayMyDearComment('ohmusama', '3 Nov 2012', 'No Comment', 'No seriously "No Comment"')
    print(str(test))
