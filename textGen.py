import random

_vowels = [ 'a', 'ae', 'ai', 'e', 'ee', 'ea', 'ei', 'i', 'ie', 'ia', 'o', 'oo', 'ou', 'u', 'ue', 'ui', 'y' ]
_constanants = [ 'b', 'c', 'ch', 'ck', 'd', 'f', 'g', 'gh', 'h', 'j', 'k', 'k', 'kl', 'm', 'n', 'ng', 'p', 'pn', 'ps', 'qu', 'r', 's', 'st', 'sh', 'ss', 'sl', 't', 'tz', 'tt', 'th', 'v', 'w', 'x', 'z']

def BuildWord(letters):
    '''
    Builds a Random word
    @arg letters    is the number of letters the word will be long
    @returns        the word as a string
    '''


    #choose if the first letter is a vowel
    if letters == 1:
        vowel = True
    else:
        vowel = random.random() > 0.5  

    #build word bits
    wordBits = []
    for i in range(letters):
        if vowel:
            wordBits.append(random.choice(_vowels))
            vowel = random.random() > 0.95
        else:
            wordBits.append(random.choice(_constanants))
            vowel = random.random() < 0.90
    return ''.join(wordBits)


def BuildPhrase(words, period = True):
    '''
    Builds a phrase
    @arg words      is the number of words that will be created in the phrase
    @arg period     is if to end the phrase with a peroid, defaults to True
    @returns        the phrase as a string
    '''
    wordList = []
    for i in range(words):
        word = BuildWord(random.randint(1, 4) + random.randint(0, 2) + random.randint(0, 2))
        if i == 0:
            wordList.append(word.capitalize())
        else:
            wordList.append(word)

    phrase = ' '.join(wordList)
    if period:
        phrase = phrase + '.'

    return phrase

def BuildParagraph(phrases = 4):
    '''
    Builds a paragraph
    @arg phrases    the number of phrases to build into the paragraph
    @returns        the paragraph as a string
    '''

    phraseList = []
    for i in range(phrases):
        phraseList.append(BuildPhrase(random.randint(2, 4) + random.randint(1, 5) + random.randint(0, 6)))

    return ' '.join(phraseList)

if __name__ == '__main__':
    print('\nBuilding Words:\n')
    for i in range(10):
        print( BuildWord(random.randint(1, 4) + random.randint(0, 3) + random.randint(0, 3)) )

    print('\nBuilding Phrases:\n')
    for i in range(10):
        print( BuildPhrase(random.randint(2, 4) + random.randint(1, 5) + random.randint(0, 6)) )

    print('\nBuildig Pharagraphs:\n')
    for i in range(10):
        print( BuildParagraph() )
