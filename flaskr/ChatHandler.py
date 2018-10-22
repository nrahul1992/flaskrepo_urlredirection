import nltk

from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from random import randint


def parentController(usertext):
    tokens = parseText(usertext)


def parseText(usertext):
    tokens = [t for t in usertext.split()]
    processedCleanTokens = []
    print("python tokens are ---- ", tokens)
    clean_tokens = tokens[:]
    sr = stopwords.words('english')
    for token in tokens:
        if token in sr:
            clean_tokens.remove(token)
    print("clean tokens are ---- ", clean_tokens)
    for tok in clean_tokens:
        processedCleanTokens.append(removePunctuationMarks(tok))
    print("fresh clean tok is ----", processedCleanTokens)
    freq = nltk.FreqDist(clean_tokens)
    print("frequency is ---- ", freq)
    for key, val in freq.items():
        print(str(key) + ':' + str(val))
    lemmatizedTokens = lemmatizeText(processedCleanTokens)
    print('lemmatized Tokens are ----', lemmatizedTokens)
    return lemmatizedTokens

def sayHi():
    greetings = ["Hello!", "It’s nice to meet you.", "Hi!", "Hi, How are things with you?", "What’s new?", "It’s good to see you.", "Good day", "Howdy!", "Hey", "What’s up?", "How’s it going?", "What’s happenin’?", "What’s happening"]
    randomnumber = randint(0, len(greetings) - 1)
    greet = greetings[randomnumber]
    return greet

def lemmatizeText(tokens):
    lemmatizedTokens = []
    for token in tokens:
        lemmatizedTokens.append(WordNetLemmatizer().lemmatize(token, 'v'))
    return lemmatizedTokens

def removePunctuationMarks(text):
    # define punctuation
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    # remove punctuation from the string
    no_punct = ""
    for char in text:
        if char not in punctuations:
            no_punct = no_punct + char
    # display the unpunctuated string
    print("processed string is ----", no_punct)
    return no_punct
