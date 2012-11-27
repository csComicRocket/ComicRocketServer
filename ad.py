
class Ad:

    _text = ""

    def __init__(self, text):
        self._text = text

    def __str__(self):
        return self._text


if __name__ == '__main__':
    test = Ad("This is a test")
    print(str(test))
